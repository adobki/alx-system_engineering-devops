#!/usr/bin/env ruby
puts ARGV[0].scan(/\b[\d]{3}[\s-]?[\d]{3}[\s-]?[\d]{3}[\s-]?[\d]\b/).join
