#!/usr/bin/env ruby
#puts ARGV[0].scan(/\[[ft][a-z]{1,4}:[\+\-].{1,16}\]/).join
var = ARGV[0].scan(/\[[ft][a-z]{1,4}:[\+\-]?.{1,16}\]/).join
var = var.sub(/\[\w{4}:/, "")
var = var.sub(/\[\w{2}:/, "")
var = var.sub(/\[\w{5}:/, "")
var = var.sub(/\]/, ",")
var = var.sub(/\]/, ",")
var = var.sub(/\]/, ",")
var = var.sub(/,$/, "")
puts var
