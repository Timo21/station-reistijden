server <- function(input, output) {

  # Reactive element that will be reloaded when input changes
  stations <- reactive({
    stations_raw %>%
      mutate(color = case_when(
        naam_lang %in% input$steden ~ 'blue',
        naam_lang %in% reachable_stations() ~ 'green',
        TRUE ~ 'red')
      )
  })

  reistijden_below_max <- reactive({
    reistijden_raw %>%
      filter(traveltime <= input$max_reistijd)
  })

  reachable_stations <- reactive({
    reistijden_below_max() %>%
      filter(naam_to %in% input$steden) %>%
      group_by(naam_from) %>%
      summarize(n = n()) %>%
      filter(n == length(input$steden)) %>%
      ungroup() %>%
      pull(naam_from)
  })

  # Plot using the df() reactive
  output$stations_kaart <- renderLeaflet({
    leaflet() %>%
      addProviderTiles(providers$Stamen.TonerLite,
                       options = providerTileOptions(noWrap = TRUE)
      ) %>%
      addAwesomeMarkers(data = stations(), icon = makeAwesomeIcon(icon = 'no-icon', markerColor = ~color), label=~naam_lang) %>%
      setView(5.6, 52.3, zoom = 7)
  })
}