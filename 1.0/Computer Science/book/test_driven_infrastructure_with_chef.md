# Test Driven Infrastructure with Chef

An introduction to automated infrastructure and how to apply test driven techniques to
infrastructure, by Stephen Nelson-Smith.

## The Philosophy of Test-Driven Infrastructure

Two fundamental rules:

1. Infrastructure can and should be treated as code.
2. Infrastructure developers should adhere to the same principles of professionalism as other
   software developers.

Treating infrastructure as code means: repeatability, automation, agility, scalability, reassurance,
and disaster recovery.

Infrastructure code should strive for the same good qualities as application code: modularity,
composability, extensibility, flexibility, repeatability, declaration, abstraction, and idempotence.

And you'll need to perform the same actions as you do with application code: design, collective
ownership, code reviews, code standards, refactoring, and testing.

## An Introduction to Chef

See <http://www.opscode.com/chef/> for latest install instructions or run:

    curl -L https://www.opscode.com/chef/install.sh | sudo bash

This will install the programs:

* `Ohai` - system profiling
* `chef-apply` - lightweight config tool to perform single command
* `chef-shell` - an interactive REPL
* `chef-solo` - standalone config management tool to be used without the server, for simple deploys
* `chef-client` - agent that runs on systems managed by Chef to communicate with the server
* `knife` - multipurpose tool to faciliate system automation, deployment, and integration

Chef is a framework, tool, and API:

* framework - provides libraries for managing almost every resource there is
* tool - see the program list above for more details about installed tools
* API - Chef is a client/server web services that is driven via a RESTful API (knife is the client)

**Chef is simply an API, an index, and a dependency resolver.**

A huge advantage of using Chef is the community that supports it. There are pre-existing recipes
that can do the heavy lifting for you.

### Use Chef to Install User on Local Machine via `chef-apply`

1. Create `tdi.rb` file:
2. Read docs for user resource: <http://docs.opscode.com/chef/resources.html#user>
3. Declare a resource in `tdi.rb` to create user `tdi`

    user 'tdi' do
      action :create
      comment 'Test Driven Infrastructure'
      home '/home/tdi'
      supports manage_home: true
    end

4. Run `sudo chef-apply tdi.rb` to create user on local machine
5. Verify user installed with `getent passwd | grep tdi`
6. Add another resource `dotfile` to drop off `.tdi` file

    dotfile '/home/tdi/.tdi' do
      action :create
      content 'bogus'
    end

7. Run `chef-apply` again
8. Observe failures
9. Replace resource `dotfile` with `file` and run `chef-apply` again
10. Replace `file` resource with `template` resource

    template '/home/tdi/.tdi' do
      action :create
      source 'tdi-bashfile'
    end

11. Run `chef-apply`

### Use Chef to Install IRC Client via `chef-solo`, recipes, cookbooks, and run lists

1. Run `chef-solo` without any configuration, what's the output?

    ...
    FATAL: Chef::Exceptions::CookbookNotFound: No cookbook found in ["/var/chef/cookbooks", ...],
    make sure cookbook_path is set correctly
    ...

2. Run `knife help cookbook` and create cookbook `irc`

    $ knife cookbook create irc -o .
    $ ls -1F irc/

3. Read the documentation at: <http://docs.opscode.com/resource_package.html>,
   <http://docs.opscode.com/resource_cookbook_file.html>,
   <http://docs.opscode.com/resource_directory.html>
4. Open `irc/recipes/default.rb` and replace it with user resource

    user 'tdi' do
      action :create
      comment "Test Driven Infrastructure"
      home "/home/tdi"
      manage_home true
    end

5. Add resource to install `irssi` package

    package 'irssi' do
      action :install
    end

6. Add resource to create `.irssi` directory in `tdi` user's home directory

    directory '/home/tdi/.irssi' do
      owner 'tdi'
      group 'tdi'
    end

7. Add resource for `~/.irssi/config`

    cookbook_file '/home/tdi/.irssi/config' do
      source 'irssi-config'
      owner 'tdi'
      group 'tdi'
    end

    # files/default/irssi-config
    servers = (
      {
        address = "irc.freenode.net";
        chatnet = "Freenode";
        ...
      }
    )
    ...

8. Search docs site for `run list`: an ordered list of roles/recipes to run in an exact order
9. Create a `solo.rb` config file and specify cookbook path

    $ mkdir ~/.chef
    $ echo "cookbook_path ENV['HOME']" > ~/.chef/solo.rb

10. Run `chef-solo` to converge the node with default recipe from irc cookbook

    $ sudo chef-solo --config ~/.chef/solo.rb --override-runlist 'recipe[irc]'

11. Login as "tdi" and launch your IRC client

We created an IRC recipe in `irc/recipes/default.rb`, which installed a user and irssi package along
with some configuration. We used the `--config` and `--override-runlist` to override Chef's defaults
for cookbook and runlist locations. Think of a cookbook as a collection of recipes.

### Install Git with Nodes and Cookbook Dependencies

1. Read docs for `knife cookbook site`

    $ cd
    $ mkdir ~/cookbooks
    $ echo "cookbook_path "#{ENV['HOME']}/cookbooks" > ~/.chef/solo.rb
    $ mv ~/irc ~/cookbooks

2. Download `git` recipe from community site

    $ knife cookbook site download git
    $ tar xzvf git-*.tar.gz -C cookbooks/

3. Read `metadata.rb` and download dependent cookbooks

    %w{ dmg build-essential yum windows }.each do |cookbook|
      depends cookbook
    end
    depends "runit", ">= 1.0"

    $ for dep in dmg build-essential yum windows runit; do
    >   knife cookbook site download $dep;
    >   tar xzvf $dep*gz -C cookbooks;
    > done

4. Ensure all cookbooks are on the cookbook path

    $ cd cookbooks
    $ grep depends */metadata.rb
    ...
    depends chef_handler
    ...
    $ knife cookbook site download chef_handler && tar xzvf chef*gz -C cookbooks

5. Search docs for `dna.json` and create it with run list

    # ~/.chef/dna.json
    {
      "run_list": ["recipe[irc]", "recipe[git]"]
    }

6. Run `chef-solo`

    $ sudo chef-solo --config ~/.chef/solo.rb --json-attributes ~/.chef/dna.json

7. Clone `https://github.com/opscode/chef-repo.git`
8. Create `chef-repo` and set remote origin, keep your infrastructure code in Git repo

    $ cd chef-repo
    $ git remote set-url origin git@github.com:atlanta-cookbooks/tdi-example
    $ git push -u origin master

## Using Chef with Tools

This chapter covers on how to aid your infrastructure code using common tools: Ruby, VirtualBox,
Vagrant. Along the way, you'll learn about `chef-client`, roles, nodes, and running chef server.

### Ruby

1. Create Opscode community login and setup account: <http://community.opscode.com/>

    # will give you 3 files: example.pem, validation.pem, knife.rb
    $ mv *.pem knife.rb chef-repo/.chef/

2. Download `knife.rb` configuration file and setup local environment

    $ knife configure client /tmp
    ...
    Writing client.rb
    Writing validation.pem

3. Run `chef-client` with `dna.json` file and upload cookbooks to Chef server

    $ sudo chef-client -j .chef/dna.json
    ... Missing Cookbooks: irc, git ...
    $ knife cookbook upload -a
    $ sudo chef-client -j .chef/dna.json

4. Download `chruby`, `ark`, and `ruby_build` cookbooks into `chef-repo` and upload to Chef server

    $ knife cookbook site download chruby # do same for ark, ruby_build
    $ tar xvf *.gz -C ~/chef-repo/cookbooks
    $ knife cookbook upload {ark,ruby_build,chruby}

5. Create a `role` and upload to Hosted Chef

    # in developer.rb
    name "developer"
    description "For Developer machines"
    run_list(
      "recipe[irc]",
      "recipe[git]",
      "recipe[chruby::system]"
    )

    default_attributes(...)

    $ knife role from file developer.rb # uploads to Chef server

6. Update the node's run list

    $ knife node edit ubuntu
    $ knife node edit centos
    $ knife node show centos -r
    romanesco:
      run_list: role[developer]

7. Run `chef-client` and verify user has Ruby installed

    $ sudo chef-client
    ... install packages ...
    $ ruby --version
    ruby 1.9.3p429

### VirtualBox

1. Install Chef Rubygem

    $ gem install chef

2. Install VirtualBox cookbook

    $ cd
    $ knife cookbook site download virtualbox
    $ tar xzvf virtualbox*gz -C chef-repo/cookbooks

3. Resolve dependencies and cookbooks, upload cookbooks to Chef server

    $ cd ~/chef-repo
    $ knife cookbook site download apt
    $ tar xzvf apt*gz -C chef-repo/cookbooks
    $ knife cookbook upload {apt,virtualbox}

4. Update `developer.rb` to add VirtualBox, upload role to Chef server

    # added to developer.rb run_list
    "recipe[virtualbox]"

    $ knife role from file roles/developer.rb

5. Run `chef-client`
6. Verify VirtualBox with `vboxmanage list vms`

### Vagrant

1. Install `vagrant` cookbook

    $ cd
    $ knife cookbook site download vagrant
    $ tar xzvf vagrant*gz -C chef-repo/cookbooks

2. Create a role for platform and configure download URL

    # in roles/debian.rb
    name "debian"
    description "Attributes specific to Debian platform family"
    run_list()

    default_attributes(
      "vagrant" => {
        "url" => "http://files.vagrantup.com/packages/7e400d00a3c5a0fdf2809c8b5001a035415a607b"
      }
    )

3. Add `vagrant` recipe to run list for developer role, upload to Chef server

    # added to developer.rb run_list
    "recipe[vagrant]"

    $ knife role show developer
    $ knife node show ubuntu -r

    $ knife role from file roles/{debian,developer}.rb
    $ knife cookbook upload vagrant

4. Run `chef-client`
5. Add Vagrant box called `opscode-centos-6.4-yourarch`, initialize it

    $ vagrant box add opscode-centos-6.4-x86_64 https://opscode-vm.s3.amazonaws.com/vagrant/opscode_centos-6.4_provisionerless.box
    $ mkdir /tmp/vagrant-example
    $ cd /tmp/vagrant-examle
    $ vagrant init opscode-centos-6.4-x86_64

6. Launch Vagrant box and connect to it

    $ vagrant up
    $ vagrant ssh

7. Destroy, recreate, and reconnect

## An Introduction to TDD and BDD

This chapter convinces you to use TDD/BDD for your code. TDD is based on the cycle: Red, Green,
Refactor. Its benefits include:

1. Preventing scope from growing
2. Reveals design problems
3. Builds trust
4. Helps programmers get into a rhythm

Whereas TDD helps programmers write correct code, BDD helps developers solve business problems. It
helps to write code that matters.

## A Test-Driven Infrastructure Framework

Test-driven infrastructure should be MASCOT:

* Mainstream
* Automated
* Side effect aware
* Continuously integrated
* Outside-in
* Test-first

The loop for developing infrastructure code becomes:

* writing tests
* running tests
* provisioning machines
* feedback

## Test-Driven Infrastructure: A Recommended Toolchain

This chapter covers the toolset which can be used for TDD and a brief overview of each.

### Berkshelf

Berkshelf is similar to Bundler, except it resolves dependencies for Chef cookbooks. It also aims to
simplify the workflow required to interact with a Chef server (less knife commands).

    $ gem install berkshelf
    $ berks help
    $ cd cookbooks/irc
    $ berks init
    $ berks install

    $ berks configure # create a new Berkshelf configuration file
    $ berks upload [COOKBOOKS] # upload cookbook to Chef Server
    $ berks apply ENVIRONMENT # apply cookbooks to Chef environment

### Test Kitchen

It isn't for writing tests, but provides a framework for verifying the state of a node.

    $ gem install test-kitchen
    $ kitchen

Use Test Kitchen to:

* create - brings instance into existence and boots it
* converge - installs Chef and sandbox for testing
* setup - sets up for test harnesses
* verify - runs any test suites that have been written
* destroy - destroys instance and returns host into clean state

### Chefspec

The purest, fastest, and most lightweight unit testing approach.

    $ gem install chefspec
    $ knife cookbook create_specs netcat -o .
    $ cat netcat/spec/default_spec.rb
    require 'chefspec'
    
    describe 'netcat::default' do
      let(:chef_run) { ChefSpec::ChefRunner.new.converge 'netcat::default' }
      it 'should do something' do
        pending 'Your recipe examples go here.'
      end
    end
    $ rspec