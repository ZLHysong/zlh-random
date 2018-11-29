# HTML5 Authoring with Mark Lassoff  
  
## Section 6: Google Fonts  
For much of the early years of the web typeface selection was very limited. For a font to display, the font had to be installed on the end users' machine.  Because of this, most web developers and designers stuck to the basics-- Times New Roman, Arial, and so on.

Over the past few years, several technologies have been introduced to provide designers with a wider variety of typefaces to choose from.

> Most people use the terms "font" and "typeface" interchangeably. In reality, these terms have different meanings. "Typeface" refers to the design of type.  Baskerville is a typeface.  "Font" refers to the physical file that holds the typeface information.  So next time, you can correctly say that you're downloading a font so that you can install at typeface.

Google Fonts is one of the options that have appeared in recent years to give designers more control over the appearance of type within their digital documents.


After completing this section you will:   

 - [ ] Navigate the Google Fonts Site 
 - [ ] Selecting Fonts to Use
 - [ ] Adding Google Fonts Code to Your HTML
 - [ ] Understanding Font Varients in Google Fonts


### Watch This:  HTML5 Section 006 Video  

As always your course videos are available on YouTube, Roku, and other locations. However, only those officially enrolled have access to this course guide, can submit assignments, work with the instructor, and get this guide.  

Watch the section video at https://www.youtube.com/watch?v=dualjljhEUE

## Navigating the Google Fonts Site
The Google Fonts site is, not surprisingly, located at https://fonts.google.com/. The interface is easy to use and designed to help you narrow down the fonts you have to choose from through filters located in the right side of the interface.

![Google Fonts Interface](https://s3.amazonaws.com/coursewareframework/html5authoring/Screen+Shot+2018-10-15+at+8.22.11+PM.png)

The soft and filter features allow you to find just the right typeface. First, you can make entire categories of fonts visible or hide them by adjusting the check marks.  For example, if you only wanted to see sans-serif typefaces, you could remove all the check marks except sans-serif.

Below the categories, you can adjust the manner in which the individual typefaces are sorted and the languages available.  Finally, there are sliders for elements like thickness and width that allow you to refine the available fonts.

Pointing at any individual typeface category with your mouse will yield additional options.

![Font Details](https://s3.amazonaws.com/coursewareframework/html5authoring/Screen+Shot+2018-10-15+at+8.33.55+PM.png)

From the first drop-down, you can choose to see a Sentence, Paragraph, Numerals, the alphabet or your custom text rendered in the active typeface. You can choose the style from the second dropdown and the size of the type displayed in the third.

Clicking on the typeface name will send you to the detail page for the selection.

![Typeface Detail page](https://s3.amazonaws.com/coursewareframework/html5authoring/Screen+Shot+2018-10-15+at+8.37.26+PM.png)
The typeface detail page will show you every glyph available in the font as well as well as the available styles. 

One feature that is unique to Google Fonts is the section of the detail page labeled "Popular Pairings."  Here, Google will suggest typefaces that work well together, allowing you to choose a secondary font for your page.

## Selecting Fonts to Use

Selecting a font that you would like to include in your digital document is easy.  On both the typeface selection screen and the typeface detail screens, you'll see a red '+' sign.  If you click it, the typeface will be added.  You'll see an indicator at the bottom of your screen where it says, "1 Family Selected".

Click the indicator, and you'll see a dialog box open at the bottom of your screen.

![Selected Font Dialog Box](https://s3.amazonaws.com/coursewareframework/html5authoring/Screen+Shot+2018-10-16+at+9.57.08+AM.png)

You can add multiple fonts by merely clicking the add font button on other typefaces through the Google Fonts interface. 

Read this dialog box carefully-- It provides all the information you need to add the Google fonts to your document.

> If consistent branding is important to you, you might want to use these typefaces in your printed documents as well. You can download the fonts by clicking the download arrow in the upper right-hand corner of the dialog box.


## Adding Google Fonts Code to Your HTML

For our sample document, I have selected a typeface called **News Cycle**.  The dialog box reveals the following:

![CSS](https://s3.amazonaws.com/coursewareframework/html5authoring/Screen+Shot+2018-10-16+at+10.14.05+AM.png)

To use the font, copy and paste the relevant code from the dialog box. The resulting HTML should be similar to the code below:

```
<!DOCTYPE html>
<html>
    <head>
        <title>Google Fonts</title>
        <link href="https://fonts.googleapis.com/css?
        family=News+Cycle:700" rel="stylesheet">
        <style>
            #container {
                font-family: 'News Cycle', sans-serif;
            }
        </style>
    </head>
    <body>
        <div id="container">
        <h1>Westport, Connecticut</h1>
        <p>Westport has a vibrant downtown and a 
        healthy commercial environment the generates 
        the feeling of a New England town with the 
        convenience of modern life. 
        Residents enjoy the quality of live due to the
        commitment to conserve the natural resources, 
        preserve traditions and support community 
        events. The town provides a wide range of 
        leisure activities and recreational venues. 
        </p>
        </div> <!-- container -->
    </body>
</html>
```
If everything is correct, the Google font will be rendered in your document.  It should look something like this in your browser:

![Google Font rendered in the brower](https://s3.amazonaws.com/coursewareframework/html5authoring/Screen+Shot+2018-10-16+at+10.20.51+AM.png)

## Understanding Font Variants
Most typefaces are comprised of several versions of the type design. These might include a thin version of the typeface, a bold version, a book version, and a very bold version.  Not all typefaces include fonts for all of these varieties.

Where there are variants available, they will be listed on the detail page for your selected font.

![Font Varients](https://s3.amazonaws.com/coursewareframework/html5authoring/Screen+Shot+2018-10-16+at+10.33.50+AM.png)
  
The screenshot above is for the typeface Niramit-- which has many variants.  To ensure we're efficient, we'd only want our document to download the individual variants that we're going to use.

The selected font dialog box will allow us to choose which variants we want to include. Inside the dialog box choose the "customize" tab for all your options to be displayed.

![Font Varients](https://s3.amazonaws.com/coursewareframework/html5authoring/Screen+Shot+2018-10-16+at+10.37.12+AM.png)

Changes you make here will be reflected in the Embed tab.  For example, after making a few selections, the embed now looks like this:

```
<link href="https://fonts.googleapis.com/css?
family=Niramit:200,400,700" rel="stylesheet">
```
The numbers (200,400,700) following the name of the font are the weights that will be loaded for the font.

To use these different weights, I'll add a font-weight rule to my CSS as demonstrated in the following code.

```
<!DOCTYPE html>
<html>
    <head>
        <title>Google Fonts</title>
        <link href="https://fonts.googleapis.com/css?
        family=Niramit:200,400,700" rel="stylesheet">
        <style>
            #container {
                font-family: 'Niramit', sans-serif;
            }
            
            h1  {
                font-weight: 200;
            }
            p   {
                font-weight:  700;
            }
        </style>
    </head>
    <body>
        <div id="container">
        <h1>Westport, Connecticut</h1>
        <p>Westport has a vibrant downtown and a healthy commercial 
        environment the generates the feeling of a New England town 
        with the convenience of modern life. Residents enjoy the 
        quality of live due to the commitment to conserve the 
        natural resources, preserve traditions and support 
        community events. The town provides a wide range of leisure 
        activities and recreational venues. </p>
        </div> <!-- container -->
    </body>
</html>
```

Here is the result with the weights correctly applied in the browser:

![Weights Applied](https://s3.amazonaws.com/coursewareframework/html5authoring/Screen+Shot+2018-10-16+at+10.51.28+AM.png)

## Submit This: The Font Feature

For this lab, you'll have to download the starter file from `https://s3.amazonaws.com/coursewareframework/html5authoring/
lab6_start.html`.  (If you are loading into your browser you can view the source code and copy it into your text editor.)

When you display the starter file in the browser it should appear like this in the browser:
![Lab Start](https://s3.amazonaws.com/coursewareframework/html5authoring/Screen+Shot+2018-10-16+at+10.59.01+AM.png)
For each of the `<div>` elements, choose a different typeface from Google Fonts.  Apply a different typeface to each element.  Also, apply a different font variant to the `<h1>` and `<p>` elements in each `<div>`.

Remember, when submitting the work, please use the following naming convention for your file: `HTMLAUTHORING_LastName_SectionNumber.html.` So, if your last name is Smith and your submitting section 8, your file name should be  `HTMLAUTHORING_Smith_8.html`.

For this course visit  [https://www.dropbox.com/request/RhW9kBDXtisq2Fsvg3hY](https://www.dropbox.com/request/RhW9kBDXtisq2Fsvg3hY)  to submit your assignments.

