#!/usr/bin/env perl -l

use strict;
use warnings;
use Data::Dumper;

my $a = 0.01;
while ( $a < 1) {
  print $a;
  $a = $a + 0.01;
}

my $b = 0.01;
my $counter = 1;

while ( $counter <= 100 ) {
  print $b;
  $b = $b + 0.01;
  $counter++;


}

