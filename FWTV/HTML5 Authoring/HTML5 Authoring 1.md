# HTML5 Authoring with Mark Lassoff
Welcome! 

Centuries ago only a privileged few learned to read and write. However, as society became more complex read and writing became necessary to navigate increasingly complex societal systems. Everyone has to pay taxes, or apply for identification or read job ads. With more accessible (even compulsory!) education, literacy rates shot up.

We're in a similar period of change now. Except reading and writing aren't the new skills necessary to navigate society. It's digital literacy now that separates the haves and the have nots.

Part of the important suite of digital skills is HTML5-- a markup language that provides the scaffolding for everything you see on the world wide web. Understanding, HTML5 (and sister technology CSS) will insure you can manage, create and update documents in the electronic world.

Keep this in mind as you progress through the course, become more digitally literate and secure your future in the digital world.

## Earning Your Certification

Completing this course will make you eligible to earn the HTML5 Specialist Designation (2019) from Framework Television. This certification is designed to represent a fundamental understanding of the HTML5 markup language and it's applicability to web development and mobile development. There are three steps to certification:

 1. Complete all of the Sections in the HTML5 Authoring Course course. You'll complete a section by reading the section guide (You're doing that now!), watching the associated video(s), and completing the code exercises.
 2. Submit a correct solution to  the Lab exercise at the end of each chapter. These are critical as learning to code is not a spectator sport!
 3. Ask an instructor to validate that you are ready for certification.  If you have completed all the sections of the course program you will be certified.

Upon earning certification, your certificate will be displayed and validated by Credential.net. You'll be provided with a URL that you can use as your proof of certification.  Credential.net will also allow you to link the certification to your LinkedIn account--- And it is highly recommended that you do so.

*Note:  As of the 2019 edition of our certification program, we are no longer requiring an online exam to earn your certification. We felt that completing the lab exercises was better proof of your programming ability than a multiple choice exam. *

### Watch This, Do This, Debug This,  Submit This
Sections of your course guides will be labeled "Watch This", "Do This", "Debug This" or "Submit This".  For these sections:

**Watch This**: This section will provide you with a link to video content that is part of the course.
**Do This**: This is an activity that you should complete.  If you have difficulty seek help in the support forum.
**Debug This**:  Sections labeled debug this contain code that has errors or problems. Make corrections to insure the code renders the expected output.
**Submit This**: This is work you must submit to earn your certification. When submitting the work please use the following naming convention for your file:   `HTMLAUTHORING_LastName_SectionNumber.html`.  So if your last name is Smith and your submitting section 8, you file name should be `HTMLAUTHORING_Smith_8.html`.

For this course go to https://www.dropbox.com/request/RhW9kBDXtisq2Fsvg3hY to submit your assignments.

## Section 1:  Creating Your First HTML5 Document

After completing this section you will:

 - [ ] Be Able to Edit Code in Your Text Editor
 - [ ] Be Able to Test Code in Your Web Browser
 - [ ] Identify the Correct File Names Mechanics for HTML5 files

### Watch This:  HTML5 Section 001 Video
As always your course videos are available on YouTube, Roku and other locations. However, only those officially enrolled have access to this course guide, are able to submit assignments, work with the instructor, and get this guide.

Watch this section video at: https://www.youtube.com/watch?v=TUOOV9A_stU

### Hello World
I like to start off with doing rather than talking. 

So open your text editor.  (For this course we recommend Brackets which you can download for free at brackets.io.)  The text editor is a program that allows you to write code without introducing a bunch of control characters as a Word Processor would. Once you open Brackets open a brand new document by clicking file and new.

We're going to save the document immediately.  (I know it might be strange to save a blank document, but there is a method to my madness!  By saving the document, we'll identify it as an HTML5 document and the text editor will color code the code for us.)

Let's click File and Save.  Navigate to wherever you'd like to save your code.  For this course I created a folder on my desktop called HTML5 Authoring.  Save your file as `helloworld.html`.

The `.html` extension is required so the computer knows what application to use to open this file.

Once you save, carefully key in the following code:

```
<!DOCTYPE html>
<html>
    <head>
        <title>Basic Document Struture</title>
    </head>
    <body>
        <h1>Hello World from your instructor, 
        Mark Lassoff</h1>
    </body>
</html>
```

You'll notice that as you type the document Brackets color codes the document separating the HTML5 tags from the content.  When your done entering the code, if you saved the document and entered everything correctly it should look like this:

![Code in Brackets](https://s3.amazonaws.com/coursewareframework/html5authoring/Screen+Shot+2018-09-28+at+5.25.40+PM.png)

Notice that the tags appear in Blue and the content appears in black.

### Viewing the Result in Your Browser
Once you've entered and double checked all the code (twice) it's time to see the result in your browser window. If you followed our recommendation and use the Brackets text editor and have the Chrome browser this will be easy.

See the lightening bold in the upper right hand corner of the Brackets interface?  That's called the Live Preview.  Click it and your browser will open and the result will appear. (Ta-Dah!).  Your browser should look similar to the screenshot below: 

![Browser Result](https://s3.amazonaws.com/coursewareframework/html5authoring/Screen+Shot+2018-09-28+at+5.36.14+PM.png)

If you have some other combination of text editor and browser, it's still easy to view (and admire) your work. Just double click the file you created and it will load in your browser.

If you're not getting the expected result it's time to debug.  Verify again that your code is correct and try to view the result in your browser window.

## Looking closer at Basic Document Structure

The code we keyed in represents the **Basic Document Structure**. This is a structure that is common to each and every HTML5 document. If you look at Amazon.com, Dell.com, or Instagram.com they all have this common structure.

```
<!DOCTYPE html>
<html>
    <head>
        <title>Basic Document Struture</title>
    </head>
    <body>
    
    </body>
</html>
```
Let's break down the component parts so you know what they are.

|Tag|Purpose  |
|--|--|
| `<!DOCTYPE html>` |This is the document type definition. It simply identifies your document as an HTML5 document. (Technically, this is not actually HTML, but SGML Standard Generalized Markup Language, but let's not get wrapped up in details).
`<html>...</html>`  | These are the HTML tags.  The first tag officially begins your HTML5 code and the latter tag ends it.
`<head>...</head>`| This is the head section of the document.  It generally contains meta information (information about your document), scripts and links.  It can also contain CSS code.
`<title>...</title>`|The title element contains the document title (obviously). The title has three purposes.  (1) It's used to label your document in browser tab. (2) It's used if your document is bookedmarked by the user and (3) It's used by search engines like Google(tm) to index your document and determine what your document is about.
`<body>...</body>`|This is the document body. This contains all the elements that appear in the document window.

A little more vocabulary:
**Opening Tag:** The first tab in a pair such as `<title>` or `<p>`.  It opens the element.
**Closing Tag:** The tag paired with the opening tag to close the element.  The closing element always contains a slash as in `</title>` or `</p>`.
**Element:** The opening tag, the closing tag and the content inside. The content may include text or other elements.

You can see how-- even at the level of the basic document structure-- the HTML5 document is a hierarchy of elements. *Keep in mind to write proper HTML5 this hierarchy must be respected and nesting must be correct.  Every tag you open must be closed (with a couple of exceptions) and the must be closed in the opposite order that they are opened.


## Editing Your Document
Let's edit the document we created before.  Let's change the document so it displays a list of my favorite tv shows from the eighties.

```
<!DOCTYPE html>
<html>
    <head>
        <title>Eighties TV</title>
    </head>
    <body>
       <p>MacGyver</p>
       <p>Magnum PI</p>
       <p>Hill Street Blues</p>
       <p>LA Law</p>
       <p>The Jeffersons</p>
    </body>
</html>
```
(I realize some of these shows overlapped other decades, but that's not the point...).

I've used the `<p>` tag which is known as the paragraph tag.  We'll learn more about it later.  Notice I simply edited the content in the title element and the body element to produce the desired output.

Before displaying this I'll save it under another file name like `eightiestv.html`.  Then I can display the new HTML document in my browser.

## Do This:
Now it's time for you to get a little practice on your own.  Start a new document called movies.html.  

Using the code above as a guide write a document that outputs the names of your five favorite movies.  Make sure to test it in the browser so you know that it is working correctly before moving on.

## Debug This:
There are errors in this code preventing it from displaying the information about the HTML5 Specialist Certification  correctly.  Fix the errors so the information displays correctly in your browser like this:

![Debug solution](https://s3.amazonaws.com/coursewareframework/html5authoring/Screen+Shot+2018-09-28+at+5.59.41+PM.png)

Here's the code to debug.
```
<!DOCTYPE html>
<html>
    <head>
        <title>Debug Me
    </head>
    <body>
        <hI>HTML5 Authoring with Mark Lassoff</hI>
        <p>The HTML5 Specialist Designation provides a 
        foundation for learning professional level 
        web development and web design. </p>
        <p>Upon completing the program, you'll earn your 
        certification. This certification is not just a 
        piece of paper to hang on your wall. 
        The HTML5 Specialist Designation is validated by 
        Credential.net. That means your certification will 
        appear on a Credential.net page accessible by private 
        URL.  You'll also be able to list the certification on 
        your LinkedIn account, so everyone can see your 
        accomplishment. (Employers have been known 
        to scan for certified individuals on LinkedIn.)</p>
    </body>
</html>
```

## Submit This: My Favorite Bands
Create an HTML5 document from scratch that is correctly formed and coded that names 5-10 of your favorite bands. The output should say "My Favorite Bands" and then include the list of bands, with each appearing on a separate line in your web browser.

Remember, when submitting the work please use the following naming convention for your file:   `HTMLAUTHORING_LastName_SectionNumber.html`.  So if your last name is Smith and your submitting section 8, you file name should be `HTMLAUTHORING_Smith_8.html`.

For this course go to https://www.dropbox.com/request/RhW9kBDXtisq2Fsvg3hY to submit your assignments.
