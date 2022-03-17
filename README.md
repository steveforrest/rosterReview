![Title, Army Roster Reviewer](static/images/project_title.png)

## Contents

* Reasons for this project
* UX
* User stories
* Future builds
* Build status
* Deployment
* Wire frame
* Languages
* Libraries and other technologies
* Testing
* Bugs
* Citations

## Reasons for this project

This site will be used to allow people to post their army lists and recieve feed back on them.

## UX

This site is designed for people who play warhammer 40k, who have made an army list and either want to brag about how good it is or get recommendations on how to improve it. It will give people the abillity to like or dislike the roster and add comments to it also.
***
I have chose to use similar Ui to other sites serving to the same community, for example: 
1. [Bolter and Chainsword](http://www.bolterandchainsword.com/)
2. [Element Games](https://elementgames.co.uk/)
3. [Battleground Gaming](https://battlegroundgaming.co.uk/)
4. [Warhammer Community](https://www.warhammer-community.com/)
***
![Index page Am i Responsive](../rosterReview/static/images/responsive_index.png)
***
![Create page Am i Responsive](../rosterReview/static/images/responsive_create.png)

***
![Detail page Am i Responsive](../rosterReview/static/images/responsive_detail.png)
***

## Future builds

Future builds will include:
* Back grounds, which will change depending on which faction has been selected.
* The ability to create a unit that is held in a model and add it into the roster rather than creating on a third party app and pasting it in or typing it out in full
* Have an image for each army which will post in roster detail template depending on which faction you pick


## Deployment

1. Ensure all the dependencies are included by adding them to the requirements.txt file by running the following command in the terminal: pip3 freeze > requirements.tx
2. Ensure the project has been fully committed and pushed to git 
3. Go to your heroku account, if you don't have one create one
4. On the home screen click on the create new app button
5. Enter a name for the project and select your region to the correct region.
6. On the next screen select settings
7. Go to config vars and click reveal config vars
8. Switch to the program file and where you are keeping your credentials copy these and then on heroku enter a name for the key and paste the code into the config vars value box and click add
9. Now scroll down to buildPacks and click add build packs
10. First select python and click save changes
11. Click back into build packs and choose node.js and click save again
12. Ensure that the Python  build pack is at the top of the list you are abe to drag and drop if you need to rearrange
13. Now select deploy
14. From the deployment method select GitHub
15. Then click on the connect to github button that appears
16. Click into the search box and search for the project name
16. Once located select connect
17. Then click deploy branch, this will then be shown in the box below
18. You can the click view to show the app in a browser

The program can be deployed automatically but i have chosen to keep it as a manual deploy so i can ensure that while i am testing and have no intention of adding more to the code currently it is better to deploy it manually meaning returning to the screen and clicking deploy branch each time you want to make any changes.

### Making a clone to run locally

* Log into GitHub.
* Select the repository.
* Click the Code dropdown button next to the green Gitpod button.
* Download ZIP file and unpackage locally and open with IDE. Alternatively copy the URL in the HTTPS box.
* Open the alternative editor and terminal window.
* Type 'git clone' and paste the copied URL.
* Press Enter. A local clone will be created.

## Wire frame

* ![Wire frame of the Index page](static/images/Wireframe_of_idex_page.png)
***
* ![Wire frame of the Roster detail page](static/images/Wireframe_of_irosterdetailpage.png)

## Languages

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)

## Libraries and other technologies

* [Heroku](https://en.wikipedia.org/wiki/Heroku)
* [Font Awesome](https://fontawesome.com/)
* [GitHub](https://github.com/)
* [Cloudinary](https://cloudinary.com/)
* [Summer Note](https://summernote.org/)
* [Crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/)
* [OAuth](https://oauth.net/)

## Testing

### Validation Testing

* [CSS testing](https://jigsaw.w3.org/css-validator/validator)
* [PEP8 testing](http://pep8online.com/)
1. Models.py tested and completed
2. Views.py tested and completed
3. Test.py tested and completed
4. Urls.py tested and completed

### Manual Testing

### Automated test

## Bugs

## Citations