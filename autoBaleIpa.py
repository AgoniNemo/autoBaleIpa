# -*- coding: utf-8 -*-
import os
import sys
import time
import hashlib
import smtplib

# 项目名字
project_name = "xxx"

# 项目根目录
project_path = "/Users/xxx/Documents/ios/project"

# 这个是plist 文件 ,用于配置打包的ipa信息的
plist_path = "/Users/xxx/Downloads/IPA.plist"

# 打包后ipa存储目录
targerIPA_parth = "/Users/xxx/Documents/ipa"


# 清理项目
def clean_project():

    os.system('cd %s;xcodebuild clean' % project_path) # clean 项目

def build_project():
    print("开始打包xcarchive")
    os.system ('cd %s;xcodebuild -list' % project_path)
    global ipa_filename
    ipa_filename = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))

    os.system ('cd %s;xcodebuild -workspace %s.xcworkspace  -scheme %s -archivePath %s/%s/%s.xcarchive archive -configuration Release || exit' % (project_path,project_name,project_name,targerIPA_parth,ipa_filename,project_name))

# 打包ipa 并且保存到targerIPA_parth,这里要注意点：ruby 版本为系统版本
def build_ipa():
        os.system ('xcodebuild -exportArchive -archivePath %s/%s/%s.xcarchive -exportPath %s/%s/%s -exportOptionsPlist %s'%(targerIPA_parth,ipa_filename,project_name,targerIPA_parth,ipa_filename,project_name,plist_path))



def main():
    # 清理项目
    clean_project()
    # 编译coocaPods项目文件并执行编译目录
    build_project()
    # 打包ipa 并且保存到targerIPA_parth
    build_ipa()


# 执行
main()
