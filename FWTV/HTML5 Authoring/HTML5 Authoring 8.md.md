
# Section 8: Lists in HTML5

After completing this section you will:

 - [ ] Be able to create unordered lists in HTML
 - [ ] Be able to create ordered lists in HTML
 - [ ] Be Able to Style Lists

**Watch This:  [HTML5 Section 008 Video](https://www.youtube.com/watch?v=AXELlDjJofQ)**

As always your course videos are available on YouTube, Roku, and other locations. However, only those officially enrolled have access to this course guide, can submit assignments, work with the instructor, and earn valuable certifications.

Watch this section video at https://www.youtube.com/watch?v=AXELlDjJofQ

## Lists

People don't read on the web. They tend to scan. So, one of the ways to get people to absorb all the material is to use lists instead of long paragraphs.  Lists are ubiquitous on the web, and the code for creating them with HTML is easy to learn.

Here we have our basic document structure with an `h1` tag to provide a heading.

    <!DOCTYPE html>
    <html> 
        <head>
            <title>Lists</title>
        </head>
        <body>
            <h1>Mark's Favorite Bands</h1>
        </body>
    </html>


There are two types of lists: unordered lists and ordered lists:

| List                |  Tag                |  Description
|--|--|--|
| Unordered List | `<ul></ul>` | Bulleted list. Used when you don't have a specific number of items.
| Ordered List | `<ol></ol>` | Numbered list items. You should use ordered lists when there is a definite number of items. (ex: 10 places I like to go, 5 things you need to know)

 Each item in a list is surrounded by list item tags: `<li></li>`

Let's add my favorite bands using an unordered list in our earlier code.

    <!DOCTYPE html>
    <html> 
          <head>
               <title>Lists</title>
           </head>
           <body>
               <h1>Mark's Favorite Bands</h1>
               <ul>
                   <li>Journey</li>
                   <li>The Cure</li>
                   <li>Doobie Brothers</li>
                   <li>Foreigner</li>
                   <li>Toto</li>
                   <li>Yes</li>
               </ul>
           </body>
    </html>

When the code for the list loads in the browser, it should appear similar to below.
![enter image description here](https://lh3.googleusercontent.com/Ky-UcGTclmwBUFYXCDb-mmjUFTiNMw3dT5FFpSEPK7zTINmDBSxA3xY1HZytfw_biTIxEp_VLgY)

The second option is the ordered list. Let's add a second list to our document that displays an ordered list.

    <!DOCTYPE html>
    <html> 
          <head>
               <title>Lists</title>
           </head>
           <body>
               <h1>Mark's Favorite Bands</h1>
               <ul>
                   <li>Journey</li>
                   <li>The Cure</li>
                   <li>Doobie Brothers</li>
                   <li>Foreigner</li>
                   <li>Toto</li>
                   <li>Yes</li>
               </ul>
               <h2>Mark's Five Favorite Places to Visit</h2>
               <ol>
                   <li>San Francisco</li>
                   <li>Portland, Maine</li>
                   <li>Seattle, Washington</li>
                   <li>Las Vegas, Nevada</li>
                   <li>Miami, Florida</li>
               </ol>
           </body>
    </html>
![enter image description here](https://lh3.googleusercontent.com/Un-jpfzpvYzL6SUp-6Z8Is1gm5SwzOPNYdbNJPQvevQ_iWPGMihoHQV70kbAUxxfXqCWATFDE5o)


## Styling lists

Several CSS rules can be used to style lists.

Let's add a class to each of our lists and add a `style` tag in the `head` so that we can add our CSS. Remember, the code inside the style tags is CSS-- not HTML. We'll use the `list-style-type` property to change how list items are displayed.

    <!DOCTYPE html>
    <html> 
          <head>
               <title>Lists</title>
               <style>
                   .music
                   {
                       list-style-type: square;
                   }
                   .places
                   {
                       list-style-type: upper-roman;
                   }
               </style>
           </head>
           <body>
               <h1>Mark's Favorite Bands</h1>
               <ul class="music">
                   <li>Journey</li>
                   <li>The Cure</li>
                   <li>Doobie Brothers</li>
                   <li>Foreigner</li>
                   <li>Toto</li>
                   <li>Yes</li>
               </ul>
               <h2>Mark's Five Favorite Places to Visit</h2>
               <ol class="places">
                   <li>San Francisco</li>
                   <li>Portland, Maine</li>
                   <li>Seattle, Washington</li>
                   <li>Las Vegas, Nevada</li>
                   <li>Miami, Florida</li>
               </ol>
           </body>
    </html>
![enter image description here](https://lh3.googleusercontent.com/FW3gi_pQ7i2WPBekECff96n8S-jLvuwAl7TD2BY-Nv7RKNMjKJQJs4ETHSWn5ux7vcCZ4OGZpB0)

For the unordered list, the `list-style-type` property changes the bullet point's shape. The default value for this property is `disc`, and other values include `circle` and `square`.

For the ordered list, we can use the same`list-style-type` property with different values such as `upper-roman` or `upper-alpha`. The value `upper-latin` is the default for an ordered list.

## Do This:

For practice, start a new document and save it as `animals.html`.

Using the code above as a guide, create a document that shows a few bullet point recommendations for walking a dog and make a second list that shows your top five favorite animals.

Make sure to test in the browser, so you know that it works correctly.

## Debug This:

There are errors in this code preventing it from displaying the information about our favorite pizzas correctly. Fix the errors, so the information displays correctly in your browser like this:

![enter image description here](https://lh3.googleusercontent.com/8iCQupqVQPLpYzZg1FOo2R8hv1CM7Di7RfM_egaMpCudWUbcbCXCSKwWCJZiddCRtSmUCvPe83U)

Here's the code to debug:

    <!DOCTYPE html>
    <html>
      <head>
        <title>Pizza</title>
        <style>
          .to-dos{
            list-style-type: circle;
          }
          .pizza-places{
            list-style-type: lower-latin;
          }
        </style>
      </head>
      <body>
        <h2>Buy the Following Pizzas</h2>
        <ul class="to-dos">
          <l1>Pepperoni</l1>
          <li>Cheese Lover</li>
        </ul>
        <li>Veggie</li>
    
        <h2>3 Best Places to Eat Pizza</h2>
        <li>Las Vegas</li>
        <lo class="pizza-places">
          <li>Milan</li>
          <li>Palermo, Italy</li>
        </lo>
      </body>
    </html>

## Submit This: Places to Visit

Create an HTML5 document from scratch that is correctly formed and coded that names five places you wish to visit and five of your favorite sites around the world. The output should include two headings, one saying “Places I Want to Visit” and the other saying "5 Best Sites in the World".  Create one of your lists as an ordered list and the other as an unordered list. Use CSS styling to change the default look for each list to make it pleasing and readable for the user.

Remember, when submitting the work, please use the following naming convention for your file: `HTMLAUTHORING_LastName_SectionNumber.html` . So if your last name is Smith and your submitting section 8, your file name should be `HTMLAUTHORING_Smith_8.html` . 

For this course go to https://www.dropbox.com/request/RhW9kBDXtisq2Fsvg3hY to submit your assignments.
