#!/usr/bin/env ruby
file = File.open(ARGV[0])
txt = file.read
msg = txt.scan(/msg:(.*?)\]/).join("\n")
puts msg 
