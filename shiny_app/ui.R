ui <- dashboardPage(
  dashboardHeader(),
  dashboardSidebar(
    selectInput("steden", "Selecteer steden:", choices=levels(stations_raw$naam_lang), multiple=TRUE,
                selected=c("Amsterdam Centraal", "Eindhoven")),
    sliderInput("max_reistijd", "Maximale reistijd (min.)", min=0, max=300, value=60)
  ),
  dashboardBody(
    tags$style(type = "text/css", "#stations_kaart {height: calc(100vh - 80px) !important;}"),
    leafletOutput("stations_kaart")
    # tableOutput("reistijden_table")
  )
)
