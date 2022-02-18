Title: blog-of-manoo
Date: 2017-11-01 17:31
Author: Manav Sharma
Nickname: manoo
Category: environment
Tags: green, nature, love
 
Finally, I wanted a lightbox. The pelican photos documentation again very helpfully provides some code to achieve this and explains what to do with it. I just had to change a few lines to get it working with my theme. Instead of linking to an external jQuery, I just sourced the local one necessary for my theme to work. I changed <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script> to <script src="{{ SITEURL }}/{{ THEME_STATIC_DIR }}/js/jquery.min.js"></script>. One more problem, however. The guide I was following said to put the magnific-popup.{js,css} files in the base of the theme directory, but the theme that I'm using checks for them in the css and js directories within a static. It will not work if you symlink the files instead of copying them. I ended up with the following code