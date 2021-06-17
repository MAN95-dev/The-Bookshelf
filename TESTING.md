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
    - Members are able to edit their own book additions, by clicking the edit button within their book modal. 

1. **To be able to write reviews about the books I would like to share.**
    - Information about product materials, measurements, safety and package are available on every listing page under the listing description.

1. **To be able to log in and out with ease.**
    - Whenever a user adds an item to their cart or adjusts the quantity in their cart the current stock level for that item is checked from its database entry. A modal will alert the user if they attempt to add more to their cart than is available in stock, and their cart will be updated to reflect the maximum number available.

1. **To be notified that I have logged in or out of my account.**
    - Each listing detail quantity selection will only go up to the maximum number in stock. 
    - Whenever an item is purchased, the stock level for it in the database is updated.
    - The shop owner can access and update stock levels from the admin panel.

1. **To be notified about changes that are made, inlcluding adding, editing, and deleting books.**
    - A text search is available on the search page. It searches through the products titles, description and tags to find and rank the results for the user.

## Manual Testing
Below is a detailed account of all the manual testing that has been done to confirm all areas of the site work as expected. 

### Testing undertaken on desktop

All steps on desktop were repeated in browsers: Firefox, Chrome and Internet Explorer and on two different desktop screen sizes.

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

1. **On running the python server, large errors appeared in terminal**
    - Any time a page was loaded, the terminal filled with around 100 lines of errors. This turned out to be a bug with Python 3.7.3 [See bug report on bugs.python.org](https://bugs.python.org/issue27682)
    - Bug was partially resolved by upgrading my version of python to python 3.7.5, although this threw new errors at me.
    - Bug finally fixed by replacing my `python manage.py runserver` command with `python manage.py runserver 8000` (with thanks to Chris Zielinski, Code Institute Mentor for this solution)

2. **Duplicate items added to OrderItems database**
    - As I was using a nested loop to compare the items in my sessions storage cart to the items in the database Order, I was ending up with duplicate items when more than 1 item was already in the database.
    - After multiple different attempts to fix the problem the solution was pretty simple: if the Order already existed I deleted all the OrderItems from the database and rebuilt them from the session variable instead.
```python
order = Order.objects.filter(customer=request.user, paid=False).first()
checkout_cart = request.session['cart']

# if new order, create instance of order
if not order:
    order = Order.objects.create(customer=request.user)

# if unpaid order exists in database already:
else:
    # get items in session storage cart
    session_cart = checkout_cart['orderItems']

    # get items currently in Order
    items_in_order = OrderItem.objects.filter(order=order)

    # delete all order items in the list
    for orderitem in items_in_order:
        orderitem.delete()

    # loop through all cart items and create new instances of OrderItem for them
    for item in session_cart:
        _id = int(item['listingId'])
        quantity = int(item['quantity'])

        # filter out items in session storage that have had their quantities reduced to 0
        if quantity > 0:
            product = Product.objects.filter(id=_id).first()
            order_item = OrderItem(order=order, product=product, quantity=quantity)
            order_item.save()
```

5. **Django code for search vectors not working with sqlite3 database**
    - The more refined search functions from `django.contrib.postgres.search`, such as `SearchQuery, SearchRank, SearchVector` would not work with my local sqlite3 database.
    - Temporarily solved this by using this simpler search code:

    ```python
    from django.db.models import Q
    results = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(tags__icontains=query))
    ```

    - Once my site was deployed, I connected to the postgres database and then replaced the above code with the more robust and accurate django postgres search code.


    ```python
    from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

    vector = SearchVector('title', weight='A') + SearchVector('description', weight='B') + SearchVector('tags', weight='C')
    query = SearchQuery(query)
    results = Product.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.1).order_by('rank')
    ```

4. **VScode unable to access postgreSQL database for testing**
    - Due to the free Hobby-dev postgres package selected when setting up the heroku database, I was not able to set the permissions necessary to alow Django to create a test database when running `manage.py test`. 
    - To fix this I reverted to accessing my sqlite3 database on my local machine for testing, and checked Travis regularly to check my tests written locally were passing when tested against the production database too.

5. **Duplicate listings showing up in All-Products view**
    - This was initially caused due to trying to sort results from the database by a boolean value (featured), but this turned out to be a known nofix issue with django. 
    - First I attempted to fix this by ordering by random, but the same problem continued.
    - Eventually I used the following code to grab both querysets for featured and not featured and concatenate them into one list to send to the page view.


    ```python
    from itertools import chain

    featured = Product.objects.filter(featured=True)
    not_featured = Product.objects.filter(featured=False)
    queryset = list(chain(featured, not_featured))
    ```

#### Unsolved bugs

1. **Sorting category results with pagination**
    - Getting the operation of pagination in shop categories in combination with the sort function throws multiple bugs and errors. The first pagination page will show correctly, but when the user tries to go to the next page the results are either reset as if the page was never sorted, or throws an error.
    - Given that the number of listings in the largest shop section is 15 - which is only 3 more than the usual pagination number of 12 - I decided to remove pagination in the shop sections and leave tackling this bug for a future release. 

## Further testing: 
1. Asked fellow students, friends and family to look at the site on their devices and report any issues they found.
2. The House of Mouse viewed on all devices and orientations available in Chrome DevTools, as well at a local tech store.