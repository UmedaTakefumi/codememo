#!/usr/bin/perl -l

use strict;
use warnings;
use Data::Dumper;

my $a = 0.01;
while ( $a <= 100) {
  print $a;
  $a = $a + 0.01;
}

my $b = 0.01;
my $counter = 0;

while ( $counter <= 100 ) {
  $b = $b + 0.01;
  $counter++;
  print $b;

}

