# Purple Pages

## An online notice board for your local community

[![Build Status](https://travis-ci.org/davebland/purple-pages.svg?branch=master)](https://travis-ci.org/davebland/purple-pages)

A full stack framework milestone project for Code Institute.

Django web application utilising Bulma CSS framework, Postgres DB, Stripe payments and Heroku hosting.

## Premise

The basic premise of this application is to create a subscription based online ‘notice board’ on which local communities can advertise events, products and services. I have drawn inspiration from a combination of printed local directory type publications (e.g. Yellow Pages) and physical community notice boards as found in the centre of villages and towns all over the UK. Users of the application will be able to advertise their event, product or service on up to 5 boards for a minimal fee.

Initially the notice boards will be segregated into UK postcode districts. Districts are the second largest geographical used by the post code system and are represented by the first 2-4 characters of a standard UK postcode (e.g. W1 xxx). There are approximately 2,960 active districts in the UK and in the real world these represent communities with an average size of 22,000 people. The list of districts will come from a free online resource, see credits.

## Demo

## UX

I wanted the design of the site to be ‘clean’ and minimal with the notice boards themselves taking cues from a physical notice board found in town/village centres, local shops etc. E.g. lots of individual ads or various sizes pinned to the board in a loose grid format.

I have decided to use Bulma CSS framework to build the front-end templates as I like the clean look of the styles and also particularly the 'columns' and ‘box’ components which lends themselves well to a notice board type look.

The colour scheme of the site will be purple and is complementing colours to reflect the application’s name.

### User Stories

## Features

- Stripe payment intents to comply with EU SCA requirements.
- Saved 'favorite' notice board either by user account or local cookie.

## Future Additions

- Advert catagories
- Live preview of advert images

## Technologies

- HTML5
- CSS3
    - Bulma.io CSS framework
- JavaScript
    - jQuery
- Python
    - Django
    - Django RelativeFilePathField
    - Pillow

## Testing

Test driven development using Django inbuilt test suite (TestCase).

### User Story Testing

## Technical Challenges

- 'No reverse match' for password reset token
- Making ajax POST requests requires including csrf token
- Storing relative file paths for template files rather than absolute (Alex Hayes package)

## Deployment

## Content

- Images from PixaBay.com under free licence

## Acknowledgements
- Draw.io wireframing tool
- Bulma.io official documentation
- jQuery official documentation
- Python and Django official documentation
- Strip APIs official documentation
- HTML5 validator https://validator.w3.org/
- CSS3 validator https://jigsaw.w3.org/css-validator/