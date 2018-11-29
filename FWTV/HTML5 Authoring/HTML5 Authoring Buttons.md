
# HTML5 Section 12:  Buttons

After completing this section, you will:

 - [ ]  Know how to use buttons in your HTML.
 - [ ]  Learn different attributes of buttons.
 - [ ]  Style your buttons.
 - [ ] Know how to add links to your buttons.

## Watch This: HTML5 Section 12 Video

As always, your course videos are available on YouTube, Roku, and other locations. However, only those officially enrolled have access to this course guide, can submit assignments, work with the instructor, and get this guide. 

Watch this section video at https://www.youtube.com/watch?v=ATHTmJ2gmz0.

## Introduction

In HTML5, buttons are necessary because they're one of the primary ways that users interact with your website. Buttons are created by changing the input element's type attribute or, more commonly, using the `button` tag.

## Buttons

We'll begin by keying in our basic document structure. 

```
<!DOCTYPE html>
<html>
    <head> 
        <title>Buttons</title>  
    </head>
    <body>
    
    </body>
</html>
```
## Simple buttons
Let's create a simple button by adding a `<button>` tag.  We'll also add some text inside the `button` tag as a text label that says `Push me!`. 
```
<!DOCTYPE html>
<html>
    <head> 
        <title>Buttons</title>  
    </head>
    <body>
        <button> Push me! </button>
    </body>
</html>
```
Now, as you can see from the screenshot below, we have a button with the text label "Push Me".

![Push me button - Output](https://lh3.googleusercontent.com/2rju9iPf_c_Q35UbbSvJUzXUdZwYsJ8wrOUB2qbtxUlAjatpCdqws7CvDgbfOmvY9MGCkhngnu4 "Push me button")


## Buttons in Forms
Often, buttons are created inside a `form` tag.  In fact, they are required to send a form to the server that is going to process it. Let's create a form that requests the user's name,  using `<input>` tag with the id attribute `userName` . We'll associate a `<label>` tag with the input tag. 
```
<!DOCTYPE html>
<html>
    <head> 
        <title>Buttons</title>  
    </head>
    <body>
    <form action="#">
        <label for="userName"> Full Name </label>
        <input id="userName" type="text">
    </form>
    </body>
</html>
```

The `action` attribute generally instructs the browser to send the data to a `PHP` form-handling page or `.Net` page. We used `#` as a value to indicates that the form is not actually processed. 

>If you want to learn to process HTML5 forms you should learn Javascript or PHP.  These languages can extract the data from the form and process it. 

Now, we'll create special types of buttons designed to be used with forms. 

**This is the older syntax for form buttons:**

```
<body>
    <form action="#">
        <label for="userName"> Full Name </label>
        <input id="userName" type="text">
        <input type="submit">
        <input type="reset">
    </form>
</body>
 ```

**This is the more current syntax you should use:**

```
<body>
    <form action="#">
        <label for="userName"> Full Name </label>
        <input id="userName" type="text">
        <button type="submit"> Submit </button>
        <button type="reset"> Reset </button>
    </form>
</body>
 ```

Here's what our form looks like in the web browser.

![](https://lh3.googleusercontent.com/b6UhGBw8CDFfb1ZKsibZtH4SDtGOSR7JBpWx_UwblnA9WO43t1kn3iQrJZ6AaPUI_IkFIU9dZIk "Buttons in Form")

The `Submit` button is used whenever you want to submit a form to the server. The `reset` button is used to clear all inputs and reset the form to the just-loaded state.

## CSS for Buttons

Let's alter the default look of the button using CSS. We declared our button with the  `push` class.

```
<!DOCTYPE html>
<html>
    <head> 
        <title>Buttons</title>  
    </head>
    <body>
        <button class="push"> Push me! </button>
    </body>
</html>
```
Next, we'll add `style` tag inside `head` tag. Using our class selector (`.push`) we can use a numnber of CSS rules to alter the default appearance of the button.

**Below several styles have been added to the button:**
```
<!DOCTYPE html>
<html>
    <head> 
        <title>Buttons</title>  
        <style>
            .push{
                font-weight: bold;
                font-size: 2.5em;
                background-color: orange;
                width: 100%;
                padding: 10px;
                color; white;
            }
        </style>
    </head>
    <body>
        <button class="push"> Push me! </button>
    </body>
</html>
```
![](https://lh3.googleusercontent.com/wqJhW1fX2zajTCvaOzV6U_P5ANzmAK1sL75zXX-6kAgeoeWSuhXmMml2ebQcu9vCrOyx7y7It4Q "CSS for Buttons")

This button has been optimized for mobile devices.  The width and height of the button make it easier for someone on a mobile device to use without accidentally tapping elsewhere on the device,.

## Button Links

There are a couple of ways to add ] function in buttons. We can use JavaScript to place a listener on the button. The JavaScript code would then react to a user tapping the button.  For now, however, we're going to use an HTML to make the button react to the user.  We'll use an  `<a>` tag, and we'll link the button to `Framework Television Site`.

```
<!DOCTYPE html>
<html>
    <head> 
        <title>Buttons</title>  
        <style>
            .push{
                font-weight: bold;
                font-size: 2.5em;
                background-color: orange;
                width: 100%;
                padding: 10px;
                color; white;
            }
        </style>
    </head>
    <body>
        <a href="http://frameworktv.com">
            <button class="push"> Push me! </button>
        </a>
    </body>
</html>
```
Now, the button is clickable and it loads the `FrameworkTV` site.

![
](https://lh3.googleusercontent.com/tcjrNEnufAsFtLShu24rEY-34w59BH_armkjCwCsi20_gBDcdbuv7BJglpSxra3MglrXKw1bJuM "FrameworkTV Site")

Again, keep in mind that the `button` tags use both opening and closing tags. 

## Do this: 

Now, it's time for you to practice on your own. Start a new HTML document and name it `infos.html`.  Using the code above as a guide,  create a form that has  `submit`  and `reset` buttons. The form contains `First Name`, `Last Name`, and `Address` using `<input>` tag.  Add some styles to the button to make them appear more attractive.

Make sure to test your file in the browser, so you know that it is working correctly before moving on.

## Debug This:

There are errors in this code preventing it from displaying the buttons correctly. Fix the errors, so the form displays correctly in your browser like this:

![](https://lh3.googleusercontent.com/1R7fz86t8xViOL39vQvBIgvW4AFpXEzGDbmq2YQFoZWm-OIJ8cVcu2XfNbRKRWVs1q0pau_z7k4 "Debug This")

Here is the code to debug:

```
<!DOCTYPE html>
<html>
    <head> 
        <title>Debug This</title>  
        <style>
            form{
                padding: 10px;
                background-color:darkgrey;
                width: 45%;
            }
            .container {
                margin: 20px;
            }
            #gender, #address{
                margin-left: 10%;
            }
            button {
                background-color: white;
                padding: 10px 25px;
                text-align: center;
                display: inline-block;
                font-size: 15px;
                margin: 4px 2px;
                cursor: pointer;
                color: black;
            }
        </style>
    </head>
    <body>
        <h1> Student's Information Form <hl>
            <div class="container">
                <label for="studentName"> Name 
                <input type="text" id="studentName" /></label>
            </div>
            <div class="container">
                <label for="studentEmail"> Email </label>
                <input type="email" id="studentEmail" />
            </div>
            <div class="container">
                <label for="gender"> Gender </label> <br/>
                <input type="radio" id="gender" 
                name="gender" value="male" checked/> Male 
                <br/>
                <input type="radio" id="gender"
                name="gender" value="female"/> Female 
                <br/>
                
            </div>
            <div class="container">
                <label for="address"> Address </label>
                 <br/>
                <textarea id="address" rows="5">
                </textarea>
            </div>
            <div class="container">
                <button type="clear" class="submit"> 
                Submit </button>
                <button type="submit" class="clear"> 
                Clear </button>
            </div>
            
        </form>
    </body>
</html>
```
## Submit This: Contact Us

Create an HTML5 document from scratch that is correctly formed and coded that displays a `Contact Us` form. There should be a field for `First name`, `Last name`, `Email`, `Contact Number`, and  `comment` with `submit`, `reset` and `Visit Us` button (Link it to your favorite site). Also, create a pleasing design for your document.

Happy coding!

Remember, when submitting the work, please use the following naming convention for your file: `HTMLAUTHORING_LastName_SectionNumber.html`. So if your last name is Smith and your submitting section 8, your file name should be `HTMLAUTHORING_Smith_8.html`.

For this course visit https://www.dropbox.com/request/RhW9kBDXtisq2Fsvg3hY to submit your assignments.
