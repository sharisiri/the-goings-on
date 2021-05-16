# The Goings On

This is a simple Bandcamp "API" that takes the last 20 tracks from your collection or wishlist and creates a simple blog with Bandcamp Iframes of those songs. It is built using Beautiful Soup, Jinja2, Github Actions for daily data refresh, and Netlify for hosting. Evertyhing is fully automated. Newly added collection / wishlist items are added to your blog each night once the Github Action runs a data refresh.

There is still some work to be done. The site not entirely mobile friendly. Some tracks do not have the iframe share option and therefore cannot be used. Track order changes after each update - Haven't found a way to sort the tracks chronologically yet.

Bandcamp, if you see this - I support you 100% and therefore the script only collects data once every night. No malicious intent at all. I only want to share the great music that I love on your platform!
