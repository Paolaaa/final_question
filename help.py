# I decided to do my final on mammals ranges and how they could be affected by climate change
#essentially I have to download maps on the range of mammals and then get the spatial data
#the maps i've found on IUCN are all interactive, I had no idea how to even begin to download the map to my terminal so I tried doing web scrapping but I dont know if it worked
#or if it is what I needed to do.
#Here is what I did

curl http://maps.iucnredlist.org/map.html?id=2055 > SA_furseal.html
ipython

In [1]: from bs4 import BeautifulSoup

In [3]: soup = BeautifulSoup(open("SA_furseal.html"))

In [4]: images = soup.find_all("img")

In [5]: for image in images:
   ...:         print image["src"]
   ...:     
images/logos/rl_logo_50.png
images/buttons/btn-home.png
images/buttons/btn-species-range-selected.png
images/buttons/btn-observation.png
images/buttons/btn-protected-areas.png
images/header/redListBanner.png
images/search/search-padding.png
images/search/search-field.png
images/loading2.gif
images/buttons/popup_btn_x.png
images/buttons/btn-circle.png
images/buttons/btn-circle.png

images/legend/{{imageurl}}
images/zoom/zoom-icon-only.png
images/legend/protectedAreas.png
images/legend/observation-flag-inaturalist-noShadow.png
images/legend/observation-flag-eol-noShadow.png
images/legend/observation-flag-gbif-noShadow.png
images/loadingSmall.gif
images/buttons/camera.png
images/iucn_logo.gif
images/ssc_logo.gif
images/buttons/btn-circle.png
images/buttons/btn-enlarge.png
images/buttons/btn-minimise.png
images/iucn_logo.gif
images/ssc_logo.gif
images/logos/protectedPlanet.jpg
images/logos/logo_facebook.png
images/logos/logo_twitter.png
images/buttons/btn_donate_now.png
images/logos/logo_protected_planet_popup.gif
images/categories/cat1a.png
images/categories/cat1b.png
images/categories/cat2.png
images/categories/cat3.png
images/categories/cat4.png
images/categories/cat5.png
images/categories/cat6.png
images/categories/undefined.png
images/loading2.gif
images/loading2.gif
images/logos/red-list-logo-popup.png
images/buttons/popup_btn_x.png

#I think there is an easier way of uploading just the map with the spatial data 
#I need but I cannot think of it.
