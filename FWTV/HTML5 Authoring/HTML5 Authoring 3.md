## Section 3:  Marking Up Text Content
Through the nineties and early 2000's the idea that the web (and by extension HTML) should become more semantic was talked about quite a bit. In fact semantic HTML became a thing. One author defines semantic HTML like this:

> _Semantic HTML_  or  _semantic_  markup is  _HTML_  that introduces meaning to the web page rather than just presentation. For example, a <p> tag indicates that the enclosed text is a paragraph. This is both  _semantic_  and presentational, because people know what paragraphs are and browsers know how to display them.
> Jennifer Kyrnin in Lifewire https://www.lifewire.com/why-use-semantic-html-3468271

As HTML5 was being developed an effort was made to include more semantic tags in the language. A properly marked up HTML document now is more self-documenting due to the use of semantic HTML.

It's important to note that while semantic HTML was a popular discussion, implementation has not been as rapid. There are still many developers who write more traditional HTML using less descriptive tags.

After completing this section you will:

 - [ ] Understand the fundamental `<p>` tag.
 - [ ] How to Apply Bold and Italics to Text using HTML
 - [ ] How to Use Semantic HTML5 Tags

### Using the Paragraph Tag
The paragraph tag is, quite obviously, used to mark up paragraphs. It is the grandaddy of semantic markup as its been around as long as HTML itself. 

The paragraph tag is likely overused in today's world of more semantic markup.  The paragraph tag has developed a role as a generic text tag used for anything from short text clips to long paragraphs.  

Using the default style sheets, browsers leave generous space between paragraph tags. Remember that if you want to just move text to the next line you also have the `<br/` tag discussed last chapter.

Let's take a look at the paragraph tag in action:
```
<!DOCTYPE html>
<html>
    <head>
        <title>Paragraphs</title>
    </head>
    <body>
        <h1>About the Instructor</h1>
        <p>Mark Lassoff has been teaching computer programming 
        and digital design since 2001.</p>
        <p>He lives in Connecticut where he is redecorating 
        his condo.  Want to help?</p>
    </body>
</html>
```
When rendered in the browser the code will appear something like this:
![P Tag Example](https://s3.amazonaws.com/coursewareframework/html5authoring/Screen+Shot+2018-10-03+at+12.35.47+AM.png)

Notice the space between the first `<p>` element and the second? Also, paragraph content is rendered in the default font at the default size unless altered by CSS, which we'll do later in the course.

### `<strong>` and `<em>`phasis
Strong and Emphasis sound like the mean the same thing-- at least from a semantic perspective. Their role is to make text appear **bold** and *italicized* respectively.  

In previous versions of HTML the tags `<b>` and `<i>`  were used for bold and italics. These tags were deprecated however and are no longer part of the current HTML5 language specification. They were replaced by `<strong>` and `<emphasis>`.

All modern browsers still correctly interpret and display display the `<b>` and `<i>` tags, however, you can't guarantee they will continue to be supported in future versions of the browsers.

These tags are in-line tags in that they don't create a line break. They can be used within a `<p>` or other container tag and just applied to the text you want to emphasize.

Let's take a look at how the `<strong>` and `<em>` tags are used in a web page.

```
<!DOCTYPE html>
<html>
    <head>
        <title>Basic Document Structure</title>
    </head>
    <body>
        <p>The instructor, <strong>Mark Lassoff</strong> has been
         teaching coding and digital design since 2001. The course
          <em>HTML5 Authoring</em> is available online.</p>
    </body>
</html>
```
The output shows the corresponding text bolded and italicized.

![Bold and Emphasis](https://s3.amazonaws.com/coursewareframework/html5authoring/Screen+Shot+2018-10-03+at+1.04.34+AM.png)

### HTML5 Semantic Tags
HTML5 introduces a number of new semantic tags. These tags are designed to better define the content they contain. For most of these new HTML5 tags, their usage is obvious from context. Many have little to no effect on how the output is displayed in the browser, but they do help achieve the goal of more semantic HTML.

There is no right or wrong way to use these new tags as long as you can justify their usage from a semantic perspective.

Here's a list of the most relevant new HTML5 tags:

 - `<article>`
-   `<aside>`
-   `<details>`
-   `<figcaption>`
-   `<figure>`
-   `<footer>`
-   `<header>`
-   `<main>`
-   `<mark>`
-   `<nav>`
-   `<section>`
-   `<summary>`
-   `<time>`

## Debug This: Semantic HTML
This code has errors that are preventing it from be displayed correctly and errors that do not effect the display of your document, but, are not proper HTML5.  
```
<!DOCTYPE html>
<html>
    <head>
        <title>Basic Document Structure</title>
    <body>
        <h1>Yonkers, New York</hI>
        <article>
            <summary>Yonker is a large suburb of New York City that
             is home to multiple attractions.</summary>
            <p><b>Yonkers</b> is the fourth most populous city in
             the U.S. state of New York, behind New York City, 
             Buffalo, and Rochester. The population of Yonkers was
             195,976 as enumerated in the 2010 United States Census
             and is estimated to have increased by 2.5% to 200,807
             in 2016.[6] It is an inner suburb of New York City,
             directly to the north of the Bronx and approximately 
             two miles (3 km) north of the northernmost point in 
             Manhattan.</p>

            <p><b>Yonkers'</b> downtown is centered on a plaza known
             as Getty Square, where the municipal government is
             located. The downtown area also houses significant 
             local businesses and non-profits, and serves as a major
             retail hub for Yonkers and the northwest Bronx.<p>

            <p>The city is home to several attractions, including the
             Untermyer Park and Gardens; Hudson River Museum; Saw 
             Mill River daylighting, wherein a parking lot was removed
             to uncover a river; Science Barge; Sherwood House; and 
             Yonkers Raceway, a harness racing track that has 
             renovated its grounds and clubhouse and added legalized 
             video slotmachine gambling in 2006 in a "racino" called 
             Empire City.</p>
        </article>
        <foot>Copyright 2018 | Framework Television</foot>
    </body>
</html>
```

## Submit This: 
Using properly formed semantic HTML5, markup the following text new stories so they display in a single document.  Make good choices with the semantic tags you use and ensure that your document displays readably for the user.
```
Hackers strike fear in almost half of big businesses
10/2/2018
A recent survey from data-tracking company Ensighten found that 46%
of all enterprise brands are concerned about data breaches after 
other large companies, such as Facebook and Uber, were hacked. 
Still, 67% have no marketing security in place, the survey found.

The world’s two largest enterprise blockchain groups join forces
10/2/2018
The Enterprise Ethereum Alliance and Hyperledger will combine forces 
to create an open-source, standards-based cross-platform project to
bring businesses distributed ledger solutions. "At Hyperledger, we're
very focused at building communities that build a set of software
products and many of those touch on and implement Ethereum-related
standards, and the EEA is focused on driving a community of 
organizations around a common set of standards and then certifying
applications against those standards," says EEA Executive 
Director Ron Resnick.

How industry experts believe AI will affect the workforce
10/2/2018
Artificial intelligence is expected to significantly affect the 
workforce in many sectors, with a 190% increase in the number of 
LinkedIn profiles listing AI skills on their account profiles since 
2015, according to LinkedIn data. The majority of experts say AI will
help make teams more effective and make better decisions, a study 
from Tata Communications found.
```

Remember, when submitting the work please use the following naming convention for your file:   `HTMLAUTHORING_LastName_SectionNumber.html`.  So if your last name is Smith and your submitting section 8, you file name should be `HTMLAUTHORING_Smith_8.html`.

For this course visit https://www.dropbox.com/request/RhW9kBDXtisq2Fsvg3hY to submit your assignments.