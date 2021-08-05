#!/usr/bin/env bash
if [ $# -eq 0 ]
  then
    tag='latest'
  else
    tag=$1
fi

# Skript für eine bessere Kontrolle über das Docker TAG System