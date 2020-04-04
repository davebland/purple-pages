# Purple Pages

## Online notice boards for local communities

[![Build Status](https://travis-ci.com/davebland/purple-pages.svg?token=s1SKguoR23tDFhPT9z49&branch=master)](https://travis-ci.com/davebland/purple-pages)

A full stack framework milestone project for Code Institute.

Django web application utilising Bulma CSS framework, Postgres relational database, Stripe payments, AWS storage and Heroku hosting.

## Premise

The basic premise of this application is to create subscription based online ‘notice boards’ on which local communities can advertise events, products and services. The inspiration from offline resources such as printed local directory publications (e.g. Yellow Pages) and physical community notice boards as found in the centre of villages and towns all over the UK.

Users will be able to browse the site as guests but will need to pay a subscription fee to advertise on a notice board. The fee is minimal (1p per day) to encourage take-up.

Initially the notice boards will be segregated into UK postcode districts. Districts are the second largest geographical used by the post code system and are represented by the first 2-4 characters of a standard UK postcode (e.g. W1 xxx). There are approximately 3000 active districts in the UK and in the real world these represent communities with an average size of 22,000 people. The list of districts comes from a free online resource, see credits.

## Demo
Browse the demo @ [https://purple-pages.herokuapp.com]

## UX

I wanted the design of the site to be ‘clean’ and minimal with the notice boards themselves taking cues from a physical notice board found in town/village centres, local shops etc. E.g. lots of individual ads of various sizes pinned to the board in a loose grid format.

I decided to use Bulma CSS framework to build the front-end templates as I like the range of UI components available and wanted to deviat from the common Bootstrap styling. Bulma was all well suited to the notice board nature of the application due to its 'column', ‘box’, ‘card’ and ‘tile’ components.

The colour scheme of the site is purple with a simple set of complementing colours to reflect the application’s name.

### User Stories
1.	Users should not need any instruction on using the site other than the visual and text cues on the pages themselves.
2.	Browsing the notice boards is straightforward (not more than 2 clicks to get to any given board) and doesn’t require a user to register for an account.
3.	A user must register on the site to design an advert but may do so without initially paying a subscription fee.
4.	When creating an advert is must be clear what input is required/allowed in each field.
5.	Once created, the advert owner must be able to edit or delete the advert. 
6.	A user must pay a subscription fee in order for their adverts to be visible on the notice boards for other site users to see.
7.	Paying a subscription fee should be a simple process but user’s must not be able to circumvent it. The subscription process should not be successful until a valid payment complete webhook has been received from Stripe.
8.	User’s must be able to change their own password and also recover a forgotten password at any time.
## Notable Features

- Secure online payments using Stripe payment intents to comply with EU SCA requirements. Includes 3D secure where applicable.
- Ability for users to save a 'favourite' notice board which replaces standard home page content. This is either stored in user profile for an authenticated user or in local cookie for a guest.
- Custom Django user model which extends the standard user with additional Purple Pages properties.
- Ability to post colour coded notifications on any page using Django messaging system.
- Customisation of the Bulma CSS framework using SASS
- Ability for user to upload custom images to adverts and have these stored in persistent datastore, AWS S3. This is achieved with django-storages and each advert having a UUID under which images are organised in the bucket.

## Future Additions

- Improved search functionality to filter by notice board
- Addition of categories to better organise adverts (e.g. product, service, social club etc.)
- Live preview of advert images on the create advert page
- Automatic resizing of uploaded images into thumbnails for better loading times
- Tiered pricing structure according to number of adverts and number of boards used

## Technologies

- HTML5
- CSS3
    - Bulma.io CSS framework (customised for Purple Pages with SASS)
- JavaScript
    - jQuery
- Python
    - Django
    - Pillow
    - Whitenoise
    - Django Storages (for AWS S3)
- Font Awesome (latest version via kit)
- Google Fonts

## Testing

Purple Pages was built from the start with test driven development in mind. Within each Django app there is a test.py with unit tests (using Django’s TestCase) that are relevant to the models, views and forms within that app. In most cases the process followed for each piece of functionality was to write a test that determined if the functionality was working (failing initially), then build the functionality and get the test to pass.

I have used Python’s coverage package to check the testing hits as much of the code as possible (collected by using ```coverage run manage.py test```). The coverage configuration file .converagerc has exclusions from coverage such as the python virtual env and Django’s own python code.

Purple Pages has 26 individual test functions giving 88% coverage of the sites code. 

There is continuous integration testing using Travis-CI. This involved setting up the repository on travis-ci.com and added .travis.yml configuration file to the project. Travis-CI automatically sets up and environment and runs ```python manage.py test``` each time a commit is made to GitHub. The current status of the test is reflected in the badge at the top of this readme. One challenge with Travis-CI was setting up the skipping of Stripe payment tests using ```@skipIf``` decorator in this environment (Stripe environment variables deliberately not added to Travis to reduce exposure of secret key).

I also used Postman for basic testing of the Stripe webhook endpoint.

### User Story Testing
1.	Users should not need any instruction on using the site other than the visual and text cues on the pages themselves. __Simple clear buttons and cues, tested by non-technical family members__
2.	Browsing the notice boards is straightforward (not more than 2 clicks to get to any given board) and doesn’t require a user to register for an account. __ Maximum 2 clicks from anywhere (Notice Boards->Board) and login nor required__
3.	A user must register on the site to design an advert but may do so without initially paying a subscription fee. __Create advert view not available to unauthenticated users, once authenticated users can create/edit adverts but get a reminder that the adverts aren’t visible until a subscription payment is made__
4.	When creating an advert is must be clear what input is required/allowed in each field. __ Fields have placeholder text where applicable and a separate instruction box that scrolls down the page with the user__
5.	Once created, the advert owner must be able to edit or delete the advert. __Clear controls for this on ‘My Ads’ page. Additional user prompt before any advert deleted__
6.	A user must pay a subscription fee in order for their adverts to be visible on the notice boards for other site users to see. __Internally the query for adverts on a board filters out any adverts where the user does not have an active subscription. Subscription can only be active is a user has made a purchase on the subscription page__
7.	Paying a subscription fee should be a simple process but user’s must not be able to circumvent it. The subscription process should not be successful until a valid payment complete webhook has been received from Stripe. __ Subscription view has defensive programming so users can select different subscription periods but a subscription will only be extended by the number of days selected. Once a payment has been made the subscription is only upated when a ``payment_intent.succeeded``` webhook is received from Stripe. This means if the user fails, abandons or loosed connection during a payment the subscription will not be erroneously updated.
8.	User’s must be able to change their own password and also recover a forgotten password at any time. __Clear link in user profile to change password. Django’s forgotten password mechanism available and customised for Purple Pages styling__

## Technical Challenges

- 'No reverse match' for password reset token
- Making ajax POST requests requires including csrf token
- Storing relative file paths for template files rather than absolute (Alex Hayes package)
- Manual import routine for postcode districts
- data-element in form fields

## Deployment

- django-storages (S3)

## Content

- Images from PixaBay.com under free licence
- List of UK postcode districts from https://www.doogal.co.uk/ - available under public licence

## Acknowledgements
- Draw.io wireframing tool
- Bulma.io official documentation
- jQuery official documentation
- Python and Django official documentation
- Strip APIs official documentation
-Postman
-TravisCI
- HTML5 validator https://validator.w3.org/