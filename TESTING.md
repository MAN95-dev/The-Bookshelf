# The Bookshelf - Testing details

[Main README.md file](README.md)

[View website on Heroku](https://the-bookshelf-milestone.herokuapp.com/)

## Table of Contents

1. [Automated Testing](#automated-testing)
    - [Validation services](#validation-services)
2. [User Stories Testing](#user-stories-testing)
3. [Manual Testing](#manual-testing)
    - [Testing undertaken on desktop](#testing-undertaken-on-desktop)
    - [Testing undertaken on tablet and phone devices](#testing-undertaken-on-tablet-and-phone-devices)
4. [Bugs discovered](#bugs-discovered)
    - [Solved bugs](#solved-bugs)
    - [Unsolved bugs](#unsolved-bugs)
5. [Further Testing](#further-testing)

## Automated Testing

### Validation Services
The following validation services and linter were used to check the validity of the website code.

- [W3C Markup Validation](https://validator.w3.org/) was used to validate HTML. 

- [W3C CSS validation](https://jigsaw.w3.org/css-validator/) was used to validate CSS.

- [JSHint](https://jshint.com/) was used to validate JavaScript.

- [PEP8 online check](http://pep8online.com/) was used to check Python code for PEP8 requirements.

- [Pylint](https://pypi.org/project/validator/) was used to validate Python.

## User Stories Testing

The following section goes through the user stories identified in the [Ux section of README.md](README.md#UX) to check that the site 
meets those needs.

**As a visitor to The Bookshelf website I expect/want/need:**

1. **To be able to easily find the information I am looking for, the layout needs to make sense so that I am not put off.**
    - Arrangement of site elements such as navbar, footer, icons, and forms conform to expected placement.

1. **The site to be laid out in a way that is easy to navigate, so that I can find what I need.**
    - The navbar offers easy navigation for the user and is clearly labeled.
    - Icons and images are used to help the user digest information quickly.

1. **The site to be responsive and navigable for various device sizes; desktop, tablet, and phone. For the content to look good on all of the devices.**
    - The use of the site has been extensively tested on desktop, tablet and phone size screens.
    - The user can load the website on mobile, tablet, and desktop devices.
    - All elements have been given a responsive design, so nothing to too squashed, squeezed or hard to read on any screen size a user might be using.
    - The navbar has a collapsed menu for tablet and mobile viewing, this makes navigation easier for smaller devices.

1. **To learn more about The Bookshelf.**
    - The home page 'Who we are' offers more information about The Bookshelf, including some of the features it has. 
    - The footer contains links to The Bookshelf's different social media accounts for more information. 

1. **To be able to connect to The Bookshelf’s social media accounts.** 
    - The footer contains links to The Bookshelf's different social media accounts, including Facebook, Instagram, and Twitter. 

1. **To be able to click on books for further information about them.**
    - Each book contains a modal button under the book cover, which can be clicked on for further information on each of the books. 
    - The modal contains the book cover image, title, author, synopsis, link to the Amazon store, and a review. 

1. **A purchase link to be provided for each book, in the event that I would like to buy it.**
    - Each book modal contains a link to the Amazon store, and has the option of hardcover, paperback, or kindle. 

1. **To be able to add, edit, and delete books that I would like to share with others.**
    - The Add book page allows members to add books that they would like to share with others, by filling in the form and submitting the 
      information. 
    - Members are able to edit their own book additions by clicking the edit button within their book modal. The edit book page allows
      members to cancel or save their edited book information. 
    - Members are able to delete their own book additions by clicking the delete button within their book modal. This brings up a modal
      askng whether thehy are sure they want to delete this book, giving them the option to cancel or delete. 

1. **To be able to write reviews about the books I would like to share.**
    - The Add book page requires members to add a review about the book they read before adding it, these reviews appear in the books 
      modal. 

1. **To be able to log in and out with ease.**
    - Both log in and log out pages are displayed in the navbar, making it easy to do both functions. 
    - The log in form is able to store your username and password if desired, making it easier and faster to log in. 

1. **To be notified that I have logged in or out of my account.**
    - When a member logs into their account, they are taken to their profile page, where a flash message displays 'Welcome, (Username)'.
    - When logged out, a flash message displays 'You have been logged out', and bringing them back to the log in page. 

1. **To be notified about changes that are made, inlcluding adding, editing, and deleting books.**
    - Flash messages have been designed to notify members when any changes have been made. 
    - When a member had added a book, a flash message displays 'Book successfully added'. 
    - When a book has been edited, a flash message displays 'Book successfully updated'.
    - When a member deletes a book, a flash message displays 'Book successfully deleted'.

## Manual Testing
Below is a detailed account of all the manual testing that has been done to confirm all areas of the site work as expected. 

### Testing undertaken on desktop

All steps on desktop were repeated in browsers: Firefox, Chrome and Safari. 

#### Elements on every page

1. Navbar 
    - Clicked each link in the navbar to confirm that it leads to the correct page.
    - Confirm that when logged out the options "Register" and "Log in" are visible and that "Account" and "Log out" are not.
    - Log into the site, confirm that options "Account" and "Log out" are visible and that "Register" and "Log in" are not.
    - Click the "Shop" link in the navbar, confirm that all sections of the shop are listed in the dropdown menu.
    - Add an item to the users cart, confirm that the counter appears over the shopping cart icon with the correct number of items displays.
    - Add more than 10 items to the cart, confirm that the counter shows `9+`.
    - Delete all items from the users cart, confirm that the counter is no longer visible in the navbar.

2. Footer
    - Click subscribe button, confirmed it opens a new tab and takes the user to the correct subscription page on the MailChimp website.
    - Hover over links in the footer, confirm the color change animation works as expected.
    - Click all links in the footer, confirm that they take the user to the relevant pages within the site.
    - Click the facebook icon, confirm that it opens a new tab and takes the user to The House of Mouse facebook page.
    - Check date of copyright information, confirm year displayed matches the current year.

#### Who we are

1. Hero Slider
    - Click slider buttons, confirm that they work as expected.
    - Adjust width of browser window, confirm image is always cropped in an attractive way.

2. Call to action buttons
    - Hover over all buttons, confirm the color change and shadow on hover appear as expected.
    - Click all buttons, confirm they take the user to the correct links and open new tabs when links go away from the website.

3. Shop section images
    - Hover over each section image, confirm shadow size increases and image looks as it if is being lifted up on the page.
    - Confirm all titles laid over on images can be easily read.

4. Testimonials carousel
    - Click carousel buttons, confirm that they work as expected.
    - Check each slide to be sure the elements fit within the slider.
    - Confirm all text can be easily read.

5. Featured listings
    - Confirm that on desktop 4 featured listings are visible in one row.
    - Confirm that on tablet 6 featured listings are visible over two rows.
    - Reload the page, confirm that a new random selection of featured listings are shown.
    - Click each listing picture, confirm that it takes the user to the relevant listing detail page.

#### Log in

- Reload the login page, confirm that the message for a new account is not visible.
- Attempt to log in with a username not in the database, confirm the relevant error message is shown.
- Attempt to log in with a correct username but wrong password, confirm the relevant error message is shown.
- Log in with a correct username and password, confirm that the user is logged in and that they are redirected to their cart page.
- Try to return to the login page url when already logged in, confirm that the user is redirected to the cart page.

#### Register

- Try to go to the register url when already logged in, confirm that the user is redirected to the home page.
- Log out then go to the register page again. Confirm that the register form is displayed as expected.
- Fill in the form with a username already in the database, confirm that the user is informed that they must use a unique username.
- Fill in the email input with a non-email address, confirm the user is shown an error asking the to use an email address.
- Go into devtools, change the `type` attribute on the email form to `text`, attempt to send the form. confirm that the Django validation catches the error and tells the user to enter an email address.
- Fill in the form with two different passwords, confirm the error is caught again and the user is informed of their mistake.
- Fill in the registration for correctly, confirm that the user is automatically directed to the login page, and the message "Your account has been created `<username>`. You can now log in." is displayed above the login page. 

#### Club picks

1. Listing breadcrumbs
    - Check that breadcrumbs show the relevant category of the product listing in them.
    - Click all breadcrumb links, confirm that they take the user to the correct pages.

2. Listing details
    - Confirm that the listing title, price, and description match those in the database for the product.

3. Listing photographs
    - Click the thumbnails provided for extra images of the product. Confirm that the large photograph is updated to reflect the thumbnails clicked.
    - Confirm that the standard photograph of the product packaging, and the one provided to show scale are visible with the other listing photographs.

4. Listing information
    - Confirm that all information on measurements, materials, safety and customisations can be found on the listing detail page under the description. 
    - Click the contact page link in the listing info, confirm it takes the user to the contact page.

5. More like this
    - Check that the listings featured in the "more like this" section are from the same category as the listing detail currently open.
    - Check that the current listing is excluded from the selection of products shown.
    - Click the products in this section, confirm that their links and hover effects work as expected.
    - Click the "browse more" button, confirm it takes the user to the correct category section of the shop.

6. Quantity selection
    - Click the quantity selection. Confirm that the highest number available to select matches the number in stock of this product.

7. Add to cart button
    - Click the "add to cart" button. Confirm that the applicable modal is launched, stating the name of the product added to the cart, and that the cart counter in the navigation bar is updated to reflect the new quantity.
    - Confirm that the modal provides two buttons to the user: to go to cart or to continue shopping. Click both to confirm they operate as expected.
    - Add more to the cart from the same product, making the total go over the max number in stock. Confirm that the modal alerting the user to too many of the product in their cart is launch. Confirm that the quantity in the cart is reset to the max number in stock.

#### Your picks

- Go to account page, confirm that the title and subheading displays as expected. 
- Check that the photograph is on the left side of the screen and the text on the right. 
- Check that the proportions of the page are as expected.
- Click the "visit shop" call to action button, confirm it takes the user to the main shop page.

#### Add book

- Go to FAQs page. Confirm that each question is in the main heading font and pink, to make it easy for users to scan the questions to find the ones relevant to their needs.
- Check that the questions are clear and the answers given are sufficient.
- Click the "contact" and "subscribe" links provided on this page, confirm they take the user to the contact page.

#### Edit book

- Go to the contact page. Confirm that the contact form is laid out as expected.
- Confirm that for a logged in user the email address field has already been populated. 
- Confirm that for a user who is not logged in the email address field is blank.
- Try to send the form with no fields filled in, confirm that the user is alerted to fill in the required fields.
- Try to enter a non-email address into the email field, confirm that the user is alerted to fill in an email address.
- Send a complete form, confirm that the message is sent to my email address with all the information included.

#### Log out

- Add a new product to the users cart. Click the "log out" link in the navigation bar. Confirm that the user is logged out and their cart has been cleared.
- Click the "Log in again" link on this page, confirm that the user is taken back to the login page.
- Confirm that the footer stays stuck to the bottom of the screen even when there is not enough content on the page to push it down.

### Testing undertaken on tablet and phone devices
All steps below were repeated to test mobile and tablet specific elements on my Samsung phone and tablet, in both the firefox browser and samsung internet browser.

Responsive design was also tested in the Chrome Developer Tools device simulators on all options and orientations.

#### Elements on every page

1. Navbar 
    - Open the website on mobile, confirm that the navbar is collapsed into a burger icon
    - click the burger icon, confirm that the navbar list appears are expected.
    - Click the "Shop" dropdown menu, confirm that the shop sections are displayed. 
    - Add something to the cart, confirm that the user shopping cart icon counter appears and displays correctly.

2. Footer
    - Scroll to the bottom of the page, confirm that the footer contents is displayed as expected with the bootstrap grid.
    - No content squashed or squeezed or disproportionate in size.
    - Confirm that all links and buttons in footer are easy to click with a finger on the smallest screen sizes.

3. Shop pages
    - Confirm that the product list is displayed one on top of each other on mobile, and 3 to a row on tablet.
    - Confirm that all clicks and swipes operate as expected on touch screen.

4. Checkout pages
    - Confirm that the order summary is displayed as a closed accordion, and can be opened with a click.
    - Check that the display of elements matches the expected layout for mobile and tablet devices.

5. All pages
    - Navigate to all pages on the site, check that the layout is as expected for the screen size.
    - Check that all buttons, menus, forms and other elements are the correct proportions and easily clickable with a finger.

### Bugs discovered: 
#### Solved bugs

1. **Flash messages not displaying**
   - None of the flash messages were displaying when logging in and out. 
   - Flash messages were hidden by the navbar. 
   - To fix this I increased the top margin of the flash messages, so that they appeared below the navbar. 
  
    ```css
    .alert {
  padding: 20px;
  background-color: #f44336;
  color: white;
  opacity: 1;
  transition: 0.6s;
  margin-top: 90px;
  width: 30%;
  text-align: center;
  left: 35%;
}
    ```

2. **When running the app.py file the js file was displaying a 404 error in the terminal**
   - When running the app.py file I was getting the following message in the terminal `J"GET /%7Burl_for('static',%20filename='js/script.js')%20%7D%7D HTTP/1.1" 404`
   - The js link at the bottom of the base.html page was missing a curly bracket. When this was added the 404 error disappeared. 

3. **Alert boxes displaying flash messages won't close when the x icon is clicked**
   - Any time a flash messaged displayed, I was unable to close it. 
   - To fix this bug I added the following on click function `onclick="this.parentElement.style.display='none';"` to the alert box button. 

   ```html
   <div class="alert success flashes">
            <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span>
            <strong>{{ message }}</strong>
        </div>
    ```

4. **Modals are not updating with the correct book content**
   - When each of the book modals are clicked on, they are all appearing with the first books' content on not their own content. 
   - To fix this I gave each books' modal button a unique data-bs-target that matched the modal's id.  

5. **A book was added to the database, but was not displaying on the members profile**
   - When adding a book via the Add book page, it would display the flash message 'Book successfully added', but was not displaying on 
     the members profile. I checked the database to ensure the data had been added, and it had. 
   - This bug was fixed by changing the href in the Your picks page to access the username instead of the book_name when displaying the 
     book's image. 

     From 

 ```html
 <a href="{{ url_for('your_picks', book_name=your_picks._id) }}"></a>
 ```
    to 

 ```html
 <a href="{{ url_for('your_picks', username=your_picks._id) }}"></a>
 ```

6. **The author's name was not displaying in the book modals**
   - When opening the book modals, none of the author's names were displaying. When I checked the database 'null' was displayed next to
     author_name. 
   - In the Add book template, book_author was used in the label, name and id, instead of author_name. Once this was changed, the authors'
     names were displaying in the modals.  

7. **Horizontal scroll present on home page**
   - To fix this bug, the footer was deleted from the home page template, as the home page was extended from the base template, which already
     included the footer. 

8. **Your picks page and modal displaying incorrect names of the members who added books**
   - If a book was uploaded by another member, it does not display that members name on the Your picks page or in the modal. Instead,
     it displays the name of the member logged in. 
   - This bug was fixed by changing `{{ username }}’s review` which displayed the name of whoever was logged in, to 
     `{{ your_picks.created_by }}'s review`, which displays the name of the member who added the book. 

9. **When deleting a book, the incorrect book was deleted**
   - When deleting a book, the previous book added by a member was deleted, whether it was their book they uploaded or another member's book. 
   - This bug was fixed by appending {{ your_picks._id }} to the delete modal button's data-bs-target and the delete modal's id. 

```html
 <!-- Modal button for Delete Book modal -->
                    <button class="btn btn-danger" data-bs-target="#modal-delete{{ your_picks._id }}"
                        data-bs-toggle="modal" data-bs-dismiss="modal">Delete</button>
```

```html
<!-- Modal for Delete Book -->
    <div class="modal fade" id="modal-delete{{ your_picks._id }}" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog">
```

10. **The background color on the home page not stretching the full browser width**
    - This bug was fixed by adding the container-fluid class to the <main> element in the base.html page and deleting all container classes
      in the other templates. 

#### Unsolved bugs


## Further testing: 
1. Asked fellow students, friends and family to look at the site on their devices and report any issues they found.
2. The House of Mouse viewed on all devices and orientations available in Chrome DevTools, as well at a local tech store.