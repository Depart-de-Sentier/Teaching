#!/bin/bash
# Should be run as su

if [ -n "$1" ]; then
  echo "Creating user account for:"
  echo $1
else
  echo "Must pass username."
  exit 1
fi

useradd --create-home $1
usermod -a -G class $1
passwd $1
