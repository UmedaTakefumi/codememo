#!/usr/bin/env perl -l

use strict;
use warnings;
use Data::Dumper;

#foreach my $tmp (0.01..1) {
#  print "$tmp\n";
#
#}

#for (my $t = 0.01; $t = $t+0.01; $t<=1.0) {
#  print $t
#}

for (my $t = 0.01; $t<=1.0; $t = $t+0.01) {
  print $t
}
print "+-+-+-+-+-";

for (my $t = 0.01; $t<=1; $t = $t+0.01) {
  print $t
}
#for (my $t = 0; $t<=6; $t++) {
#  print $t
#}

