# HTML5 Tables

After completing this section, you will:

 - [ ] Know how to use tables in your HTML5 document.
 - [ ] Learn about table attributes
 - [ ] Be able to use rowspan and colspan within your tables.
 - [ ] Style your tables and make them more readable.

*** Watch This: HTML5 Section 012 Video ***

As always your course videos are available on YouTube, Roku, and other locations. However, only those officially enrolled have access to this course guide, can submit assignments, work with the instructor, and get this guide. 

Watch this section video at: https://youtu.be/gS1OqFL1Ujo

## Introduction

In the early days of the web, tables were often misused to layout web pages-- that doesn't happen anymore. Modern CSS has provided a number additional tools for laying out pages.  Now tables are strictly used to display tabular information. Think of a table of contents or a chart of your employees.   Any information that you might put in a spreadsheet, might be displayed in a table in digital design.

## Tables

We'll begin with our basic document structure, as usual.

```

    <!DOCTYPE html>
    <html>
      <head>
        <title>Tables</title>
      </head>
      <body>

      </body>
    </html>
```

Let's create a table with some historical information about computers. We'll start by adding an `<h1>`  that describes the table and below it, we'll write the `<table>` tag. To create rows in our table, we'll use a `<tr>` tag.

Now, we'll write our actual content in the `<td>` tag. Each `<td>` tag will be written inside a `<tr>` tag. Since we're making a table about computers, we'll include the labels  `Maker`, `Model` and `Year`.

```
    <body>
        <h1>Computers</h1>
        <table>
            <tr>
            <td>Maker</td> <td>Model</td> <td>Year</td>
            </tr>
        </table>
    </body>
```

As you can see in the code, the layout of the HTML5 table has been written to mirror the appearance of rows and columns. You don't have to code the table this way. However, this layout is very similar to how the table will appear in the browser. This layout gives us a visual representation for the table and aids us in seeing the result from the document.

Another common way to author with  `<td>` tags, is by putting each one on its line of code.

We'll now add some actual information to our table.

```
  <body>
    <h1>Computers</h1>
    <table>
      <tr>
        <td>Maker</td> <td>Model</td> <td>Year</td>
      </tr>
      <tr>
        <td>Commodore</td> <td>64</td> <td>1982</td>
      </tr>
      <tr>
        <td>IBM</td> <td>IBM PC Junior</td> <td>1983</td>
      </tr>
      <tr>
        <td>Apple</td> <td>Apple Lisa</td> <td>1982</td>
      </tr>
      <tr>
        <td>Apple</td> <td>Apple Macintosh</td> <td>1984</td>
      </tr>
    </table>
  </body>
```

The resulting table should appear similar to the screenshot below.

![enter image description here](https://lh3.googleusercontent.com/0bi_H5Y2juwMtuoxR049VJ0kcrazbQiRhtE-C0pobhkM6BCUTabf-wQ5YnEfLZ1VmVmiYTU0TLwX)

The table is clearly defined, and each column has a set width. You can also see how the layout in the code is similar to the table's layout in the browser. 

We can improve the table appearance by bolding the text in the first row for the column labels. We'll use the `<th>` tag, the table header tag, instead of the `<td>` tag.

```
    <table>
      <tr>
        <th>Maker</th><th>Model</th><th>Year</th>
      </tr>
      ...
    </table>
```

![enter image description here](https://lh3.googleusercontent.com/WXy1Cdk6k9cSBhmgGg0a6_9OkFtILMuG5pA8a2X6kpjbKIR11CWpkYh1kei5Q7DM7_XRFO2nZWOw)

The `<th>` tags differentiate the table's labels from the table's information.

## Table Attributes

While most table attributes are deprecated, it's essential for you to recognize them when you see them.  

The first attribute we're going to look at is the `border`.
```
    <table border="1">
    ...
    </table>
```

![enter image description here](https://lh3.googleusercontent.com/NKrMBCFMnndi1LJyS1VLVUG4RwUVZPzkGpJpu_34CsIw2GuPMUCTDQb5biRUI0fWCvXPGsbZnBUJ)

The table in the image above has an "old-school" 90's feel due to the double border lines and spacing.

Changing the value of the `border` attribute will increase the width of the outer border of the table.

The attribute `cellspacing` creates a space around each cell inside the table. The amount of space depends on the number assigned to `cellspacing`.

```
    <table cellspacing="10" border="1">
    ...
    </table>
```

![enter image description here](https://lh3.googleusercontent.com/WStTrHPNX_tRX_MovA9OZzv8ejRWVNU2-hnuj_uT5rXrprAI7a6j6d1jX_4HToO5rvO_2evlgLzF)

Another attribute that is similar to `cellspacing` is `cellpadding`. While `cellspacing` creates space ***around*** the cells of the table, the `cellpadding` attribute creates space ***within*** the cells of the table.

```
    <table cellspacing="10" cellpadding="10" border="1">
    ...
    </table>
```

![enter image description here](https://lh3.googleusercontent.com/WEAwgmJw_xkX6cf5sp8JrxeGJLHD7FwyKrzuE27Phn3Tkc84RBqmu7L9FMN78ibT_JcAIUHrik9q)

These attributes should be replaced with the more modern CSS which allows us to create the same effects just generated and more.

## Rowspan and Colspan

Some useful attributes still have their use cases for HTML5 tables. Suppose you have a cell that you want to occupy more than a single cell space.

In our computers table example, the last two rows begin with the `Apple` cell. Instead of having to write the same piece of information twice, we can delete one of them and include in the other cell a `rowspan` attribute and assign its value to two.

```
    <table>
      <tr>
        <th>Maker</th><th>Model</th><th>Year</th>
      </tr>
      ...
      <tr>
        <td rowspan="2">Apple</td><td>Apple Lisa</td><td>1982</td>
      </tr>
      <tr>
        <td>Apple Macintosh</td><td>1984</td>
      </tr>
    </table>
```

![enter image description here](https://lh3.googleusercontent.com/jOMUvpUOKLpL9t5qxtp1WaP3Bwr2MwI5PgKt4gYpZxOxwQA_EMEYja6c_7Y1e2yY6L8D9ljDxs2i)

Now the `Apple` cell occupies both rows for `Apple Lisa` and `Apple Macintosh`.

Another similar attribute is the `colspan` which allows a cell to occupy multiple columns within the same row.

```
    <table>
      <tr>
        <th>Maker</th><th>Model</th><th>Year</th>
      </tr>
      <tr>
        <td colspan="2">Commodore</td><td>1982</td>
      </tr>
      ...
    </table>
```

![enter image description here](https://lh3.googleusercontent.com/dEKYwPfC7SjI49Dq3UZRqh3Mn8QhVqkx9GpDoG--Dlbh3_gl0c81yloe-ZQ7e_ND9qAQygYrIO_L)

## CSS For Tables

To begin styling our table, we'll first add a style tag within our `head` element.

```
      <head>
        <title>Tables</title>
        <style>

        </style>
      </head>
```

We can change the style of the whole table by styling the `table` selector for the `table` tag.

```

    <style>
      table{
        background-color: #ccc;
      }
    </style>
```

![enter image description here](https://lh3.googleusercontent.com/Orc8Dau3oC-t9LKOZVnTtYc4saU5YDwDkFdfjMIR6TMIyZPeNbT836q7ZYnSYEH-89dR7s8vKFVR)


If we now want to add a border to the table, we can use the `border` property which requires three inputs. The first is the width, then the type and finally the color of the border.

We're going to add a border with a width of two pixels, with a solid outline and a black color.

```

    <style>
      table{
        background-color: #ccc;
        border: 2px solid black;
      }
    </style>
```


![enter image description here](https://lh3.googleusercontent.com/Eh-ScEXM74SbZeiKrAoGSIQeo2tNKmmF6PBlofiw3xUilbQkOInmOCwwzNqEjnRuI7N3V-2E5gkh)

The border only covers the outer edge of the table. To add a border for our `<th>`, `<tr>` and `<td>` tags, we'll need to use the appropriate selectors and add a border.

```
    <style>
      table{
        background-color: #ccc;
        border: 2px solid black;
      }

      tr, th, td {
        border: 1px solid black;
      }
    </style>
```

![enter image description here](https://lh3.googleusercontent.com/6cPdqNLJLpqNOwBq6c2kxAl12eJsF-b47SvUpaHl7lYOrErvC-kOU_z1wR0RfOaGqcjqspGmb0WX)



## Border-collapse

Since we've applied a border to each of our cells, the ugly look of a double border is still present. To remove that double border, we'll use the `border-collapse` property and set it to `collapse` in our `table` selector.

```

    <style>
      table{
        background-color: #ccc;
        border: 2px solid black;
        border-collapse: collapse;
      }

      tr, th, td {
        border: 1px solid black;
      }
    </style>

```

![enter image description here](https://lh3.googleusercontent.com/JRv2VjDQQ_bCtEH_wsru_pWFyVrguqyhDsT0gu8O_ndX5txVI6WbPc_VvW4sn-8uv-X5ljKjnJI8)

While this solves our border problem, our table now appears too tight. We'll add some padding to our content to make it more readable.


```
    <style>
      table{
        background-color: #ccc;
        border: 2px solid black;
        border-collapse: collapse;
      }

      tr, th, td {
        border: 1px solid black;
        padding: 3px;
      }
    </style>
```

![enter image description here](https://lh3.googleusercontent.com/LXOAo56JYTqjdfGMnyNS_66xD3LD16aNj_CzeAuZdybsqCfjRkQiPML-GGmpo8BTy7mPZvqExok6)

We can also change the fonts within any of the tags inside the table. Let's set the `font-family` on the `<th>` tags to `Arial` and the `font-size` to `1.2em`.

```
    <style>
      ...
      th{
        font-family: Arial;
        font-size: 1.2em;
      }
    </style>
```

![enter image description here](https://lh3.googleusercontent.com/mYKfLFA7GwjT9feM_Ofb3As31eYAqH79gXwpEkK3ydorQ96bwj6ygaZSh-QKWii-ZO7W9cb09NJG)


## Row color

Often web developers will alternate row colors in their tables to make them more readable.  Alternating row colors may seem difficult using CSS. However, we can add a class to every other row and set the background color within that class.

Let's change every other row's background into a dark blue color with white text.

```
  <head>
    <title>Tables</title>
    <style>
      ...
      .dark{
        background-color: darkblue;
        color: white;
      }
    </style>
  </head>
  <body>
    <h1>Computers</h1>
    <table>
      <tr class="dark">
        ...
      </tr>
      <tr>
        ...
      </tr>
      <tr class="dark">
        ...
      </tr>
      <tr>
        ...
      </tr>
      <tr class="dark">
        ...
      </tr>
    </table>
  </body>
```

![enter image description here](https://lh3.googleusercontent.com/d07ZGJKzZubg24iHXQbZJL6ImfB8BOfyKLB8I5RrfybgN7dN7QoVq6zG9dm67UBexotYnxl6Lr18)



## Do This:
Now, it’s time for you to get a little practice on your own. Start a new document and name it plants.html. Using the code above as a guide write a table that outputs the names of five plants along with their average lifespans.

Give the table a single lined border of your own choice of color and style.

Make sure to test it in the browser, so you know that it is working correctly before moving on.

## Debug This:
There are errors in this code preventing it from displaying the table of products correctly. Fix the errors, so the information displays correctly in your browser like this:

![enter image description here](https://lh3.googleusercontent.com/LqSiYjxtpbXilgWSINsl-m6evJwl5UJHYb367Lpw0dgZygly-V9EGYEN_mwkp5Rv-2AJ-LPJLFBP)

Here is the code to debug.

```
<!DOCTYPE html>
<html>
  <head>
    <title>Tables</title>
    <style>
      table{
        background-color: #eee;
        border: 1px solid black;
      }

      th, td {
        padding: 4px;
        border: 1px solid black;
      }

      #white{
        color: #fff;
      }
    <style>
  </head>
  <body>
    <h1>Supermarket Sales</h1>
    <table>
      <tr>
        <th>Product</th><th>Price</th><th>Sales</th>
      </tr>
      <tr class="white">
        <td>Cola</td><td>2$</td><td>50 Units</td>
      </tr>
      <td>Cereal</td><td>5$</td><td>70 Units</td>
      <tr>
        <td>Apples</td><td>8$</td><td>90 Units</td>
      </tr>
      <tr>
        <td>Bananas</td><td>6$</td><td>30 Units</td>
      </tr>
  </body>
</html>
```
## Submit This: Companies
Create an HTML5 document from scratch that is correctly formed and coded that displays a table of several companies from around the world. There should be a field for the company name, the company's country of origin, the date that it was started in and the names of its founders.

Use row colors to make the table's content easier to read and add a single line border. Also, change the default font of the table into a font of your choosing.

Remember, when submitting the work please use the following naming convention for your file: HTMLAUTHORING_LastName_SectionNumber.html . So if your last name is Smith and your submitting section 8, your file name should be HTMLAUTHORING_Smith_8.html . 

For this course go to https://www.dropbox.com/request/RhW9kBDXtisq2Fsvg3hY to submit your assignments.

