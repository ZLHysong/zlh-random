## Section 2:  Using HTML5 Heading Tags
Heading Tags are commonly used to mark up headings within a document. Within complex documents there are often several levels of headings to concern yourself with. HTML actually offers six levels of heading so even the most complex scientific documents can be rendered correctly.

After completing this section you will:

 - [ ] Be able to use HTML5 Headings 

## HTML5 Headings
Examine the following code.

```
<!DOCTYPE html>
<html>
    <head>
        <title>Headings</title>
    </head>
    <body>
        <h1>The Coders' Daily Bugle</h1>
        <h2>All the news thats fit to code</h2>
        <h3>This is an h3.</h3>
        <h4>This is an h4.</h4>
        <h5>This is an h5.</h5>
        <h6>This is an h6.</h6>
    </body>
</html>
```
This code demonstrates all six available levels of heading within HTML. `<h1>` is designed to surround the most important heading on the page. `<h2>` should be used for subheadings (or second level headings). For less important headings in the document you'll use `<h3>` through `<h6>`. 

When rendered in the browser the html should appear similar to the screenshot below.
![Heading Tags](https://s3.amazonaws.com/coursewareframework/html5authoring/Screen+Shot+2018-09-30+at+10.27.57+PM.png)

Very few documents use `<h4>` through `<h6>`.

> Keep in mind, that while headings are rendered larger and bolder than body text, headings are not the proper way to increase the size of text in your document. Size and boldness are simply the way the default style sheet opts to represent heading importance. You can alter this (and the appearance of any element) with CSS.
The purpose of HTML is to define the purpose of individual content elements, not the appearance of the elements. Appearance remains completely the domain of CSS (Cascading Style Sheet language).

## The Break Tag
There are two things notable about the break tag. First it's a self closing tag. Second, it's immensely useful.

The break tag is written as `<br/>`.  You'll immediately note that it looks different than any of the tags we've discussed so far.  The break tag does **not** have a closing tag. It's self closing and can have no content in side of it.  (The slash at the end indicates a self-closing or empty tag.)

It's function is to simply put a break in the text and start on the next line.  

Let's look at a quick example:
```
<p>Roses are Red<br/>
Violets are Blue<br/>
I like HTML5<br/>
And I Hope So Do you</p>
```
Due the the break tags this code would display as follows:
```
Roses are Red
Violets are Blue
I like HTML5
And I Hope So Do you
```
Note that all the text appears within the same paragraph element, but, the text is distributed on different lines due to the appearance of the `<br/>`. 

## Debug This
There are errors in this code preventing it from displaying the information about the HTML5 Specialist Certification  correctly.  Fix the errors so the information displays correctly in your browser like this:
![Debugging](https://s3.amazonaws.com/coursewareframework/html5authoring/Screen+Shot+2018-09-30+at+10.49.58+PM.png)

Here's the code.  Good luck!
```
<!DOCTYPE>
<html>
    <head>
        <title>Grand Slam<title>
    </head>
        <h1>Grand Slam</h1>
        <h2>>Written By Majorie Maddox</h2>
        <p>Dreams brimming over,<br/>
           childhood stretched out in legs,<br/>
           this is the moment replayed on winter days<br/>
           when frost covers the field,<br/>
           when age steals away wishes.<br/>
           Glorious sleep that seeps back there<br/>
           to the glory of our baseball days.</p>
</html>
```
## Submit This: With Rue My Heart is Laden
**With Rue My Heart is Laden** is a famous poem by AE Houseman. The poem goes like this:

_With Rue My Heart is Laden_  
  
_For golden friends I had,_  
_For many a rose-lipt maiden_  
_And many a lightfoot lad._  
  
_By brooks too broad for leaping_  
_The lightfoot boys are laid;_  
_The rose-lipt girls are sleeping_  
_In fields where roses fade._  

_- AE Houseman_

Using the the proper HTML5 basic document structure and the tags you have learned so far (`<p>`, `<h1>` ... `</h6>`) display the poem as written above on a web page. Don't forget to include the poem title and the author.

Remember, when submitting the work please use the following naming convention for your file:   `HTMLAUTHORING_LastName_SectionNumber.html`.  So if your last name is Smith and your submitting section 8, you file name should be `HTMLAUTHORING_Smith_8.html`.

For this course go to https://www.dropbox.com/request/RhW9kBDXtisq2Fsvg3hY to submit your assignments.
