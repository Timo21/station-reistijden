# Load libraries
library(shiny)
library(stringr)
library(ggplot2)
library(dplyr)
library(leaflet)
library(shinydashboard)

# Load all R functions in the resources folder
for (file in list.files('r_resources')){
  source(file.path('r_resources', file))
}

# Load in the data that should be globally available
stations_raw <- read.csv(file.path('data', 'grote_stations.csv'))
reistijden_raw <- read.csv(file.path('data', 'reistijden.csv'))




