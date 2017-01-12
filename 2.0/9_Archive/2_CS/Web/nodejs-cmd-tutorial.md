# Node.js 命令行程序实例教程

这个学期 Coding Bootcamp 最后一个作业是用 Node.js 做一个小程序，正好借此机会学习一下 Node.js。这个教程主要是关于如何用 Node.js 做命令行程序的，涉及服务器和 web 的部分基本上是没有的。

## Node.js 基本介绍

简单的说 Node.js 就是运行在服务端的 JavaScript。

+ Node.js 是一个基于Chrome JavaScript 运行时建立的一个平台。
+ Node.js是一个事件驱动I/O服务端 JavaScript 环境，基于 Google 的V8 引擎，V8 引擎执行 Javascript 的速度非常快，性能非常好。

换个角度来看，JavaScript 是脚本语言，脚本语言都需要一个解析器才能运行。对于写在 HTML 页面里的 JavaScript，浏览器充当了解析器的角色。而对于需要独立运行的 JavaScript，Node.js 就是一个解析器。

Node.js 的作者说，他创造 Node.js 的目的是为了实现高性能 Web 服务器，他首先看重的是事件机制和异步IO模型的优越性，而不是 JavaScript。但是他需要选择一种编程语言实现他的想法，这种编程语言不能自带IO功能，并且需要能良好支持事件机制。JavaScript 没有自带IO功能，天生就用于处理浏览器中的 DOM 事件，并且拥有一大群程序员，因此就成为了天然的选择。

开发之前的准备工作这里不赘述，在[官网](https://nodejs.org/en/)上有详细的文档

唯一需要提的是最好安装一个 [NVM](https://github.com/creationix/nvm)。NVM 的全称是 Node Version Manager，之所以需要这个工具，是因为 Node.js 的各种特性都没有稳定下来，所以我们经常由于老项目或尝新的原因，需要切换各种版本。

安装也很简单

`curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.25.2/install.sh | bash`

装好之后在终端中输入 `$ node`，REPL(read–eval–print loop) 应该就出来了，那我们就成功了。

## 任务介绍

既然是实例教程，我们需要有一个例子，这里我们要做的事情有四个

1. 读入一个[文本文件](http://www.gutenberg.org/cache/epub/45/pg45.txt)
2. 根据读入的内容进行一些数据计算
	+ 词数
	+ 行数
	+ 列出所有的词以及对应的出现次数，降序排列
	+ 出现次数最多的十个 trigram
	+ 出现次数最多的 trigram 与之后的十个出现次数最多的 trigram 的编辑距离，列出比较的对象以及编辑距离的值 
3. 把得到的结果写成 HTML 文件保存在本地
4. 支持自定义参数调用，例如可以在命令行中输入文件名

## Hello World

配置好了环境，就可以开始这次的任务了，但是开始之前，万变不离其宗，先要来一发 hello world。步骤如下

1. 新建一个文件夹
2. 文件夹里新建一个名为 `hello.js` 的文件

文件内容

```javascript
console.log('Hello World, this is wdx');
```

用命令行进入刚才新建的文件夹，然后 `node hello.js`，可以看到输出了 `Hello World, this is wdx`，于是第一步就完成了。

## 一：读取文件

知道了基本的执行操作，我们可以开始读入指定的 txt 文件，下载好[文件](http://www.gutenberg.org/cache/epub/45/pg45.txt) 并放在同一个文件夹里，就可以利用 node.js 自带的库来进行操作了。

然后我们新建另外一个文件 `parser.js`，具体的操作请参看注释，这里用了一些变量名方便以后拓展，也有把函数作为参数传给另外的函数，这个是函数式编程的做法，在这里不展开。

```javascript
// load file system module
var fs = require('fs');

var filename = 'pg45.txt';

console.log('loading content from ' + filename);

// read the contents of the file into memory
fs.readFile(filename, function (err, buffer) {
    // If an error occurred, throwing it will
    // display the exception and end our app
    if (err) throw err;

    // buffer is a Buffer, convert to string
    var text = buffer.toString();
    console.log('loading done');
});
```

载入之后我们就可以对内容进行操作了

## 二：数据统计

### 行数/词数/词频

完成了上一节，我们已经拿到了文本的内容，可以开始具体操作了。直接在刚才的文件后面继续添加代码，统计单词数量，行数，以及每个单词出现的次数。

```javascript
console.log('start processing content');

// the stats variable
var linecount = 0;
var wordcount = 0;

// get line count
var lines = text.split('\n');
linecount = lines.length;

// get words count and their number of appearance
var index = {};
lines.forEach(function(line){
   var words = line
               .replace(/[.,?!;()"-]/g, " ")
               .replace(/\s+/g, " ")
               .toLowerCase()
               .split(" ");
   // count words
   wordcount += words.length;
   // build index dictionary
   words.forEach(function (word) {
       if (word != ''){
           if (!(index.hasOwnProperty(word))){
               index[word] = 0;
           }
           index[word]++;
       }
   });
});

// change dict to array for sort
var indexarr = [];
var i = 0
for (var key of Object.keys(index).sort()){
   indexarr[i] = [key, index[key]];
   i += 1;
}

// sort the array
indexarr = indexarr.sort(function(x,y){
   return y[1] - x[1];
});

console.log('processing content done');
console.log('--------statistics--------');

console.log('Line Count: ' + linecount);
console.log('Word Count: ' + wordcount);
for (var j = 0; j < 10; j++){
   console.log(indexarr[j]);
}
```

### Trigram 统计

Triagram 的定义可以从 [wiki](https://en.wikipedia.org/wiki/Trigram) 找到，其实就是遍历一次所有的单词，三个三个一组，然后统计频率，其实逻辑和前面统计词频是一样的。所以思路是增加一个存所有单词的数组，然后遍历生成字典，然后字典转数组进行排序找到前十一个，这样就可以显示前十个，并且计算第一个和后面十个的编辑距离。

我们先修改一下之前统计词频的代码

```javascript
// get words count and their number of appearance
var index = {};
// save each word to an array
var wordarr = [];
// save the trigram to an dictionary
var trigrams = {};

lines.forEach(function(line){
   var words = line
               .replace(/[.,?!;()"-]/g, " ")
               .replace(/\s+/g, " ")
               .toLowerCase()
               .split(" ");
   // count words
   wordcount += words.length;
   // build index dictionary
   words.forEach(function (word) {
       if (word != ''){
           wordarr.push(word);
           if (!(index.hasOwnProperty(word))){
               index[word] = 0;
           }
           index[word]++;
       }
   });
});
```

接下来就主要处理这个 `wordarr` 数组了，利用 `slice()` 和 `join()` 的功能就可以很方便地实现：

```javascript
// get trigram
for (var j = 0; j < wordarr.length-3; j++){
   var temp = wordarr.slice(j, j+3).join(' ');
   if (!(trigrams.hasOwnProperty(temp))){
       trigrams[temp] = 0;
   }
   trigrams[temp]++;
}

// change dict to array for sort
var trigramsarr = [];
var i = 0
for (var key of Object.keys(trigrams).sort()){
   trigramsarr[i] = [key, trigrams[key]];
   i += 1;
}

// sort the array
trigramsarr = trigramsarr.sort(function(x,y){
   return y[1] - x[1];
});

// Get Top 11 trigrams
trigramtop11 = trigramsarr.slice(0,11);
```

再运行一下，就可以看到结果没有问题了，就剩最后一个问题，编辑距离

### 编辑距离

编辑距离又叫 levenshtein 距离，是一种比较两个字符串相似程度的算法，具体的原理不赘述，利用动态规划就可以解决，我们这里写一个函数方便调用。

```javascript
function levenshtein(a, b) {
	var al = a.length + 1;
	var bl = b.length + 1;
	var result = [];
	var temp = 0;
	// 创建一个二维数组
	for (var i = 0; i < al; result[i] = [i++]) {}
	for (var i = 0; i < bl; result[0][i] = i++) {}		
	for (i = 1; i < al; i++) {
		for (var j = 1; j < bl; j++) {
			// 判断最上方和最左方数字是否相等
			temp = a[i - 1] == b[j - 1] ? 0 : 1;
			// result[i - 1][j] + 1 左方数字
			// result[i][j - 1] + 1 上方数字
			// result[i - 1][j - 1] + temp 左上方数字
			result[i][j] = Math.min(result[i - 1][j] + 1, result[i][j - 1] + 1, result[i - 1][j - 1] + temp);
		}
	}
	return result[i-1][j-1];
}
```

然后只要在代码中调用这个函数即可

```javascript
// Calculate edit distance and sort by distance value
// create an array to save the result
var resultstr = [];
for (var j = 1; j < 11; j++){
   var dis = levenshtein(trigramtop11[0][0], trigramtop11[j][0]);
   var str = "[" + trigramtop11[0][0] + "] vs [" + trigramtop11[j][0] + "]: ";
   resultstr.push([str, dis]);
}
resultstr.sort(function(x, y){
   return y[1] - x[1];
});
```

这样一来，第二步也就完成了

## 三：输出 HTML

写入文件我们同样使用 fs 模块，思路是我们先把要展示的内容存到一个 string 中，然后一次写入到 html 文件里，就算完成。具体代码比较简单，这也是之前为什么我要把所有的计算结果都换存起来的原因，方便写入。注意 HTML 输出的格式即可，代码如下：

```javascript
console.log('Creating HTML content');

var htmlcontent = '<html><head><title>' + filename + ' Analysis Result</title><head>';
htmlcontent += '<body><h1>' + filename + ' Analysis Result</h1>';
htmlcontent += '<h2>Line Count: ' + linecount + '</h2>';
htmlcontent += '<h2>Word Count: ' + wordcount + '</h2>';
htmlcontent += '<h2>Trigram Frequency (Top 10)</h2><ol>';
for (var j = 0; j < 10; j++){
   htmlcontent += '<li>' + trigramtop11[j] + '</li>';
}
htmlcontent += '</ol><h2>Trigram Edit Distance</h2><ol>';
for (var j = 0; j < 10; j++){
   htmlcontent += '<li>' + resultstr[j] + '</li>';
}
htmlcontent += '</ol><h2>Word Frequency</h2><ul>';
for (var j = 0; j < indexarr.length; j++){
   htmlcontent += '<li>' + indexarr[j] + '</li>';
}
htmlcontent += '</ul></body></html>';


console.log('')
console.log('Generating HTML file');
var filenamearr = filename.split('.');

fs.writeFile(filenamearr[0] + '-result.html', htmlcontent, function(err){
   if (err){
       return console.error(err);
   }
   console.log('Generation Success');
   console.log('Filename: ' + filenamearr[0] + '-result.hmtl');
   console.log('---------------------');
   console.log('All Job Done');
});
```

## 四：传入参数

现在我们读入的内容是写死在代码里的，如果我们需要更灵活，从命令行传入参数的话，还需要对代码做一些改动。现在我们调用 `parser.js` 的方式是使用 `node parser.js`，现在需要实现用 `node parser.js pg45.txt` 这样的方式，可以把代码改为：

```javascript
var filename = process.argv[2];

if (filename == undefined){
    console.log('No input argument, use default file');
    filename = 'pg45.txt';
}
```

这里也做了一些错误处理以防用户没有输入第二个参数，如果命令是 `node parser.js pg45.txt`，那么参数实际是 `['node', '/path/to/parser', 'pg45.txt']`

## 总结

至此，所有的任务就已经完成了，具体的代码可以在[这里](https://github.com/wdxtub/11601-summary-stat-nodejs)找到，这个教程不涉及网络，也只使用了 fs 一个模块，但是对于熟悉 javascript 和 nodejs，是一个很好的练习。

## 参考资料

+ [Node.js 命令行程序开发教程](http://www.ruanyifeng.com/blog/2015/05/command-line-with-node.html)
+ [用Node.js创建命令行工具](http://www.html-js.com/article/A-day-to-learn-JavaScript-create-commandline-tools-with-Nodejs)

