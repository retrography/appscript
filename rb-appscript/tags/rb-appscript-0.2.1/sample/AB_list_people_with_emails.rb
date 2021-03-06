#!/usr/bin/env ruby

# Lists the name and email(s) of every person in Address Book with one or more email addresses.

require "appscript"
include Appscript

people_ref = app('Address Book').people[its.emails.ne([])]
p people_ref.name.get.zip(people_ref.emails.value.get)