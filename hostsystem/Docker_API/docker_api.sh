#!/bin/bash

echo "Vorhandene Container"
docker ps

echo "Zustand der Knotenpunkte"
docker node ls


echo "vorhandene volumes"
docker volume ls


echo "vorhandene Netzwerke"
docker network ls