This repo is examples of webcrawlers built using the Scrapy python framework.  For more details about Scrapy..

 - [Scrapy Framework](https://github.com/scrapy/scrapy/)
 - [Wiki](https://github.com/scrapy/scrapy/wiki)

Gibyellow Spider
====================================

Simple Scrapy spider for [Gibyellow](http://gibyellow.gi/)

------------

About Scrapy
------------

Scrapy is a fast high-level screen scraping and web crawling framework, used to crawl 
websites and extract structured data from their pages. It can be used for a wide range 
of purposes, from data mining to monitoring and automated testing.

ref: http://www.scrapy.org

Setup Guide
-----------

// Remove previous installation of Python 2.7
sudo rm -R /System/Library/Frameworks/Python.framework/Versions/2.7

// Install Homebrew
$ ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"

// Add to profile
~/.bashrc
export PATH=/usr/local/bin:/usr/local/sbin:$PATH

// Fresh install Python 2.7
brew install python

// Add to profile
~/.bashrc
export PATH=/usr/local/share/python:$PATH

// Install Scrapy library with pip (pip should have been installed by brew when you installed python)
pip install Scrapy

//Setup spider project
scrapy startproject gibyellow

//To run each spider individually
cd gibyellow
scrapy crawl gibyellow

etc..

!!WARNING!!
===========
You should not scrape any website that you do not own unless you have gotten consent from the 
webmaster of the site.  Using these scripts, can and will cause you to be blacklisted if used 
abusively and/or incorrectly.  This repository is for reference purposes only and should not be
run on a live environment.
