# Mac 命令行指南

## 显示/隐藏 隐藏文件

    defaults write com.apple.finder AppleShowAllFiles -bool true
    defaults write com.apple.finder AppleShowAllFiles -bool false

## 想接收最新开发者版本，在Terminal输入：

    sudo defaults write /Library/Preferences/com.apple.SoftwareUpdate CatalogURL https://swscan.apple.com/content/catalogs/others/index-10.10seed-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog.gz

## 想接收最新公测版版本，在Terminal输入：

    sudo defaults write /Library/Preferences/com.apple.SoftwareUpdate CatalogURL https://swscan.apple.com/content/catalogs/others/index-10.10beta-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog.gz

## 停止接收开发者或公测版，只接收正式版推送方法，在Terminal输入：

    sudo softwareupdate --clear-catalog
