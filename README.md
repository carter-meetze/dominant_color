# dominant_color
Get the dominant color of an image

This script has 4 functions:
  - img2hex: 
    - input: path of image
    - output: dominant color in HEX format
  - img2rgb:
    - input: path of image
    - output: dominant color in RGB
  - img_url2hex:
    - input: url of image
    - output: dominant color in HEX format
  - img_url2rgb:
    - input: url of image
    - output: dominant color in RGB format
    
Optionally, you can enter a hue threshold as a kwarg. Any color under X hue will be filtered out. Can be entered as a decimal between 0.01 - 0.99

Example:

input: print(img_url2hex('https://images.unsplash.com/photo-1506744038136-46273834b3fb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjExMDk0fQ&dpr=2&auto=format&fit=crop&w=416&h=312&q=60', hue=.3))

output: #3d7693
