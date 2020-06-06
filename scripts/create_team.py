import json
from collections import OrderedDict
from random import Random

from faker import Faker


def create_team(num=1, team_size=Random().randint(3, 10), company=Faker().last_name(), team_name=None):
    def get_personality():
        return Faker().random_elements(elements=OrderedDict([
            ("ISFJ", 13.8)
            , ("ESFJ", 12.3)
            , ("ISTJ", 11.6)
            , ("ISFP", 8.8)
            , ("ESTJ", 8.7)
            , ("ESFP", 8.5)
            , ("ENFP", 8.1)
            , ("ISTP", 5.4)
            , ("INFP", 4.4)
            , ("ESTP", 4.3)
            , ("INTP", 3.3)
            , ("ENTP", 3.2)
            , ("ENFJ", 2.5)
            , ("INTJ", 2.1)
            , ("ENTJ", 1.8)
            , ("INFJ", 1.5)
        ]), length=1, unique=False)[0]

    def get_status():
        return Faker().random_elements(elements=OrderedDict([
            ("Single", 20)
            , ("In A Relationship", 30)
            , ("Married", 25)
            , ("Divorced", 25)
        ]), length=1, unique=False)[0]

    def get_ethnicity():
        return Faker().random_elements(elements=OrderedDict([
            (["light", "Asian"], 0.03),
            (["medium-dark", "Pacific Islander"], 0.02),
            (["dark", "Black or African American"], 0.11),
            (["medium", "Hispanic or Latino"], 0.15),
            (["medium-light", "White"], 0.69)
        ]), length=1, unique=False)[0]

    def get_job():
        member['jobavatar'] = jobs[f"{member['gender']}:{member['skin_tone']}:{occupation}"]
        member_sum = int(member['jobavatar']['SalaryMax']) - int(member['jobavatar']['SalaryMin'])
        range_low = int(member['jobavatar']['SalaryMin']) + ((level - 1) * .25) * member_sum
        range_high = int(member['jobavatar']['SalaryMin']) + (level * .25) * member_sum
        member['salary'] = '${:,.2f}'.format(Random().randrange(range_low, range_high)) + "/yr"

    foods = {
        "Grapes": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/grapes_1f347.png",
        "Melon": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/melon_1f348.png",
        "Watermelon": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/watermelon_1f349.png",
        "Tangerine": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/tangerine_1f34a.png",
        "Lemon": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/lemon_1f34b.png",
        "Banana": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/banana_1f34c.png",
        "Pineapple": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/pineapple_1f34d.png",
        "Mango": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/mango_1f96d.png",
        "Red Apple": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/red-apple_1f34e.png",
        "Green Apple": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/green-apple_1f34f.png",
        "Pear": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/pear_1f350.png",
        "Peach": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/peach_1f351.png",
        "Cherries": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/cherries_1f352.png",
        "Strawberry": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/strawberry_1f353.png",
        "Kiwi Fruit": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/kiwifruit_1f95d.png",
        "Tomato": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/tomato_1f345.png",
        "Coconut": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/coconut_1f965.png",
        "Avocado": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/avocado_1f951.png",
        "Eggplant": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/aubergine_1f346.png",
        "Potato": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/potato_1f954.png",
        "Carrot": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/carrot_1f955.png",
        "Ear of Corn": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/ear-of-maize_1f33d.png",
        "Hot Pepper": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/hot-pepper_1f336.png",
        "Cucumber": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/cucumber_1f952.png",
        "Leafy Green": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/leafy-green_1f96c.png",
        "Broccoli": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/broccoli_1f966.png",
        "Garlic": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/garlic_1f9c4.png",
        "Onion": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/onion_1f9c5.png",
        "Mushroom": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/mushroom_1f344.png",
        "Peanuts": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/peanuts_1f95c.png",
        "Chestnut": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/chestnut_1f330.png",
        "Bread": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/bread_1f35e.png",
        "Croissant": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/croissant_1f950.png",
        "Baguette Bread": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/baguette-bread_1f956.png",
        "Pretzel": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/pretzel_1f968.png",
        "Bagel": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/bagel_1f96f.png",
        "Pancakes": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/pancakes_1f95e.png",
        "Waffle": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/waffle_1f9c7.png",
        "Cheese Wedge": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/cheese-wedge_1f9c0.png",
        "Meat on Bone": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/meat-on-bone_1f356.png",
        "Poultry Leg": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/poultry-leg_1f357.png",
        "Cut of Meat": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/cut-of-meat_1f969.png",
        "Bacon": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/bacon_1f953.png",
        "Hamburger": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/hamburger_1f354.png",
        "French Fries": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/french-fries_1f35f.png",
        "Pizza": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/slice-of-pizza_1f355.png",
        "Hot Dog": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/hot-dog_1f32d.png",
        "Sandwich": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/sandwich_1f96a.png",
        "Taco": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/taco_1f32e.png",
        "Burrito": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/burrito_1f32f.png",
        "Stuffed Flatbread": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/stuffed-flatbread_1f959.png",
        "Falafel": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/falafel_1f9c6.png",
        "Egg": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/egg_1f95a.png",
        "Cooking": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/cooking_1f373.png",
        "Shallow Pan of Food": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/shallow-pan-of-food_1f958.png",
        "Pot of Food": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/pot-of-food_1f372.png",
        "Green Salad": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/green-salad_1f957.png",
        "Popcorn": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/popcorn_1f37f.png",
        "Butter": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/butter_1f9c8.png",
        "Canned Food": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/canned-food_1f96b.png",
        "Bento Box": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/bento-box_1f371.png",
        "Rice Cracker": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/rice-cracker_1f358.png",
        "Rice Ball": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/rice-ball_1f359.png",
        "Cooked Rice": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/cooked-rice_1f35a.png",
        "Curry Rice": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/curry-and-rice_1f35b.png",
        "Steaming Bowl": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/steaming-bowl_1f35c.png",
        "Spaghetti": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/spaghetti_1f35d.png",
        "Roasted Sweet Potato": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/roasted-sweet-potato_1f360.png",
        "Oden": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/oden_1f362.png",
        "Sushi": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/sushi_1f363.png",
        "Fried Shrimp": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/fried-shrimp_1f364.png",
        "Fish Cake": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/fish-cake-with-swirl-design_1f365.png",
        "Moon Cake": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/moon-cake_1f96e.png",
        "Dango": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/dango_1f361.png",
        "Dumpling": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/dumpling_1f95f.png",
        "Fortune Cookie": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/fortune-cookie_1f960.png",
        "Chinese Food": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/takeout-box_1f961.png",
        "Crab": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/crab_1f980.png",
        "Lobster": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/lobster_1f99e.png",
        "Shrimp": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/shrimp_1f990.png",
        "Squid": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/squid_1f991.png",
        "Oyster": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/oyster_1f9aa.png",
        "Soft Ice Cream": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/soft-ice-cream_1f366.png",
        "Shaved Ice": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/shaved-ice_1f367.png",
        "Ice Cream": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/ice-cream_1f368.png",
        "Doughnut": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/doughnut_1f369.png",
        "Cookie": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/cookie_1f36a.png",
        "Birthday Cake": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/birthday-cake_1f382.png",
        "Shortcake": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/shortcake_1f370.png",
        "Cupcake": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/cupcake_1f9c1.png",
        "Pie": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/pie_1f967.png",
        "Chocolate Bar": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/chocolate-bar_1f36b.png",
        "Candy": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/candy_1f36c.png",
        "Lollipop": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/lollipop_1f36d.png",
        "Custard": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/custard_1f36e.png"}

    jobs = {
        "Male:light:Counselor": {
            "Title": "Deaf Man: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/deaf-man-light-skin-tone_1f9cf-1f3fb-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Counselor",
            "SkinTone": "light",
            "Location": "School",
            "SalaryMin": "60000",
            "SalaryMax": "92000"
        },
        "Male:medium-light:Counselor": {
            "Title": "Deaf Man: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/deaf-man-medium-light-skin-tone_1f9cf-1f3fc-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Counselor",
            "SkinTone": "medium-light",
            "Location": "School",
            "SalaryMin": "60000",
            "SalaryMax": "92000"
        },
        "Male:medium:Counselor": {
            "Title": "Deaf Man: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/deaf-man-medium-skin-tone_1f9cf-1f3fd-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Counselor",
            "SkinTone": "medium",
            "Location": "School",
            "SalaryMin": "60000",
            "SalaryMax": "92000"
        },
        "Male:medium-dark:Counselor": {
            "Title": "Deaf Man: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/deaf-man-medium-dark-skin-tone_1f9cf-1f3fe-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Counselor",
            "SkinTone": "medium-dark",
            "Location": "School",
            "SalaryMin": "60000",
            "SalaryMax": "92000"
        },
        "Male:dark:Counselor": {
            "Title": "Deaf Man: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/deaf-man-dark-skin-tone_1f9cf-1f3ff-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Counselor",
            "SkinTone": "dark",
            "Location": "School",
            "SalaryMin": "60000",
            "SalaryMax": "92000"
        },
        "Female:light:Counselor": {
            "Title": "Deaf Woman: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/deaf-woman-light-skin-tone_1f9cf-1f3fb-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Counselor",
            "SkinTone": "light",
            "Location": "School",
            "SalaryMin": "60000",
            "SalaryMax": "92000"
        },
        "Female:medium-light:Counselor": {
            "Title": "Deaf Woman: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/deaf-woman-medium-light-skin-tone_1f9cf-1f3fc-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Counselor",
            "SkinTone": "medium-light",
            "Location": "School",
            "SalaryMin": "60000",
            "SalaryMax": "92000"
        },
        "Female:medium:Counselor": {
            "Title": "Deaf Woman: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/deaf-woman-medium-skin-tone_1f9cf-1f3fd-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Counselor",
            "SkinTone": "medium",
            "Location": "School",
            "SalaryMin": "60000",
            "SalaryMax": "92000"
        },
        "Female:medium-dark:Counselor": {
            "Title": "Deaf Woman: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/deaf-woman-medium-dark-skin-tone_1f9cf-1f3fe-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Counselor",
            "SkinTone": "medium-dark",
            "Location": "School",
            "SalaryMin": "60000",
            "SalaryMax": "92000"
        },
        "Female:dark:Counselor": {
            "Title": "Deaf Woman: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/deaf-woman-dark-skin-tone_1f9cf-1f3ff-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Counselor",
            "SkinTone": "dark",
            "Location": "School",
            "SalaryMin": "60000",
            "SalaryMax": "92000"
        },
        "Male:light:Actor": {
            "Title": "Prince: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/prince_emoji-modifier-fitzpatrick-type-1-2_1f934-1f3fb_1f3fb.png",
            "Gender": "Male",
            "OccupationName": "Actor",
            "SkinTone": "light",
            "Location": "Studio",
            "SalaryMin": "19000",
            "SalaryMax": "200000"
        },
        "Male:medium-light:Actor": {
            "Title": "Prince: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/prince_emoji-modifier-fitzpatrick-type-3_1f934-1f3fc_1f3fc.png",
            "Gender": "Male",
            "OccupationName": "Actor",
            "SkinTone": "medium-light",
            "Location": "Studio",
            "SalaryMin": "19000",
            "SalaryMax": "200000"
        },
        "Male:medium:Actor": {
            "Title": "Prince: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/prince_emoji-modifier-fitzpatrick-type-4_1f934-1f3fd_1f3fd.png",
            "Gender": "Male",
            "OccupationName": "Actor",
            "SkinTone": "medium",
            "Location": "Studio",
            "SalaryMin": "19000",
            "SalaryMax": "200000"
        },
        "Male:medium-dark:Actor": {
            "Title": "Prince: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/prince_emoji-modifier-fitzpatrick-type-5_1f934-1f3fe_1f3fe.png",
            "Gender": "Male",
            "OccupationName": "Actor",
            "SkinTone": "medium-dark",
            "Location": "Studio",
            "SalaryMin": "19000",
            "SalaryMax": "200000"
        },
        "Male:dark:Actor": {
            "Title": "Prince: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/prince_emoji-modifier-fitzpatrick-type-6_1f934-1f3ff_1f3ff.png",
            "Gender": "Male",
            "OccupationName": "Actor",
            "SkinTone": "dark",
            "Location": "Studio",
            "SalaryMin": "19000",
            "SalaryMax": "200000"
        },
        "Female:light:Actor": {
            "Title": "Princess: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/princess_emoji-modifier-fitzpatrick-type-1-2_1f478-1f3fb_1f3fb.png",
            "Gender": "Female",
            "OccupationName": "Actor",
            "SkinTone": "light",
            "Location": "Studio",
            "SalaryMin": "19000",
            "SalaryMax": "200000"
        },
        "Female:medium-light:Actor": {
            "Title": "Princess: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/princess_emoji-modifier-fitzpatrick-type-3_1f478-1f3fc_1f3fc.png",
            "Gender": "Female",
            "OccupationName": "Actor",
            "SkinTone": "medium-light",
            "Location": "Studio",
            "SalaryMin": "19000",
            "SalaryMax": "200000"
        },
        "Female:medium:Actor": {
            "Title": "Princess: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/princess_emoji-modifier-fitzpatrick-type-4_1f478-1f3fd_1f3fd.png",
            "Gender": "Female",
            "OccupationName": "Actor",
            "SkinTone": "medium",
            "Location": "Studio",
            "SalaryMin": "19000",
            "SalaryMax": "200000"
        },
        "Female:medium-dark:Actor": {
            "Title": "Princess: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/princess_emoji-modifier-fitzpatrick-type-5_1f478-1f3fe_1f3fe.png",
            "Gender": "Female",
            "OccupationName": "Actor",
            "SkinTone": "medium-dark",
            "Location": "Studio",
            "SalaryMin": "19000",
            "SalaryMax": "200000"
        },
        "Female:dark:Actor": {
            "Title": "Princess: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/princess_emoji-modifier-fitzpatrick-type-6_1f478-1f3ff_1f3ff.png",
            "Gender": "Female",
            "OccupationName": "Actor",
            "SkinTone": "dark",
            "Location": "Studio",
            "SalaryMin": "19000",
            "SalaryMax": "200000"
        },
        "Male:light:Artist": {
            "Title": "Man Artist: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-artist-type-1-2_1f468-1f3fb-200d-1f3a8.png",
            "Gender": "Male",
            "OccupationName": "Artist",
            "SkinTone": "light",
            "Location": "Sunrise",
            "SalaryMin": "20000",
            "SalaryMax": "100000"
        },
        "Male:medium-light:Artist": {
            "Title": "Man Artist: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-artist-type-3_1f468-1f3fc-200d-1f3a8.png",
            "Gender": "Male",
            "OccupationName": "Artist",
            "SkinTone": "medium-light",
            "Location": "Sunrise",
            "SalaryMin": "20000",
            "SalaryMax": "100000"
        },
        "Male:medium:Artist": {
            "Title": "Man Artist: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-artist-type-4_1f468-1f3fd-200d-1f3a8.png",
            "Gender": "Male",
            "OccupationName": "Artist",
            "SkinTone": "medium",
            "Location": "Sunrise",
            "SalaryMin": "20000",
            "SalaryMax": "100000"
        },
        "Male:medium-dark:Artist": {
            "Title": "Man Artist: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-artist-type-5_1f468-1f3fe-200d-1f3a8.png",
            "Gender": "Male",
            "OccupationName": "Artist",
            "SkinTone": "medium-dark",
            "Location": "Sunrise",
            "SalaryMin": "20000",
            "SalaryMax": "100000"
        },
        "Male:dark:Artist": {
            "Title": "Man Artist: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-artist-type-6_1f468-1f3ff-200d-1f3a8.png",
            "Gender": "Male",
            "OccupationName": "Artist",
            "SkinTone": "dark",
            "Location": "Sunrise",
            "SalaryMin": "20000",
            "SalaryMax": "100000"
        },
        "Female:light:Artist": {
            "Title": "Woman Artist: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-artist-type-1-2_1f469-1f3fb-200d-1f3a8.png",
            "Gender": "Female",
            "OccupationName": "Artist",
            "SkinTone": "light",
            "Location": "Sunrise",
            "SalaryMin": "20000",
            "SalaryMax": "100000"
        },
        "Female:medium-light:Artist": {
            "Title": "Woman Artist: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-artist-type-3_1f469-1f3fc-200d-1f3a8.png",
            "Gender": "Female",
            "OccupationName": "Artist",
            "SkinTone": "medium-light",
            "Location": "Sunrise",
            "SalaryMin": "20000",
            "SalaryMax": "100000"
        },
        "Female:medium:Artist": {
            "Title": "Woman Artist: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-artist-type-4_1f469-1f3fd-200d-1f3a8.png",
            "Gender": "Female",
            "OccupationName": "Artist",
            "SkinTone": "medium",
            "Location": "Sunrise",
            "SalaryMin": "20000",
            "SalaryMax": "100000"
        },
        "Female:medium-dark:Artist": {
            "Title": "Woman Artist: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-artist-type-5_1f469-1f3fe-200d-1f3a8.png",
            "Gender": "Female",
            "OccupationName": "Artist",
            "SkinTone": "medium-dark",
            "Location": "Sunrise",
            "SalaryMin": "20000",
            "SalaryMax": "100000"
        },
        "Female:dark:Artist": {
            "Title": "Woman Artist: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-artist-type-6_1f469-1f3ff-200d-1f3a8.png",
            "Gender": "Female",
            "OccupationName": "Artist",
            "SkinTone": "dark",
            "Location": "Sunrise",
            "SalaryMin": "20000",
            "SalaryMax": "100000"
        },
        "Male:light:Astronaut": {
            "Title": "Man Astronaut: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-astronaut-type-1-2_1f468-1f3fb-200d-1f680.png",
            "Gender": "Male",
            "OccupationName": "Astronaut",
            "SkinTone": "light",
            "Location": "Milky Way",
            "SalaryMin": "65000",
            "SalaryMax": "150000"
        },
        "Male:medium-light:Astronaut": {
            "Title": "Man Astronaut: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-astronaut-type-3_1f468-1f3fc-200d-1f680.png",
            "Gender": "Male",
            "OccupationName": "Astronaut",
            "SkinTone": "medium-light",
            "Location": "Milky Way",
            "SalaryMin": "65000",
            "SalaryMax": "150000"
        },
        "Male:medium:Astronaut": {
            "Title": "Man Astronaut: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-astronaut-type-4_1f468-1f3fd-200d-1f680.png",
            "Gender": "Male",
            "OccupationName": "Astronaut",
            "SkinTone": "medium",
            "Location": "Milky Way",
            "SalaryMin": "65000",
            "SalaryMax": "150000"
        },
        "Male:medium-dark:Astronaut": {
            "Title": "Man Astronaut: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-astronaut-type-5_1f468-1f3fe-200d-1f680.png",
            "Gender": "Male",
            "OccupationName": "Astronaut",
            "SkinTone": "medium-dark",
            "Location": "Milky Way",
            "SalaryMin": "65000",
            "SalaryMax": "150000"
        },
        "Male:dark:Astronaut": {
            "Title": "Man Astronaut: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-astronaut-type-6_1f468-1f3ff-200d-1f680.png",
            "Gender": "Male",
            "OccupationName": "Astronaut",
            "SkinTone": "dark",
            "Location": "Milky Way",
            "SalaryMin": "65000",
            "SalaryMax": "150000"
        },
        "Female:light:Astronaut": {
            "Title": "Woman Astronaut: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-astronaut-type-1-2_1f469-1f3fb-200d-1f680.png",
            "Gender": "Female",
            "OccupationName": "Astronaut",
            "SkinTone": "light",
            "Location": "Milky Way",
            "SalaryMin": "65000",
            "SalaryMax": "150000"
        },
        "Female:medium-light:Astronaut": {
            "Title": "Woman Astronaut: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-astronaut-type-3_1f469-1f3fc-200d-1f680.png",
            "Gender": "Female",
            "OccupationName": "Astronaut",
            "SkinTone": "medium-light",
            "Location": "Milky Way",
            "SalaryMin": "65000",
            "SalaryMax": "150000"
        },
        "Female:medium:Astronaut": {
            "Title": "Woman Astronaut: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-astronaut-type-4_1f469-1f3fd-200d-1f680.png",
            "Gender": "Female",
            "OccupationName": "Astronaut",
            "SkinTone": "medium",
            "Location": "Milky Way",
            "SalaryMin": "65000",
            "SalaryMax": "150000"
        },
        "Female:medium-dark:Astronaut": {
            "Title": "Woman Astronaut: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-astronaut-type-5_1f469-1f3fe-200d-1f680.png",
            "Gender": "Female",
            "OccupationName": "Astronaut",
            "SkinTone": "medium-dark",
            "Location": "Milky Way",
            "SalaryMin": "65000",
            "SalaryMax": "150000"
        },
        "Female:dark:Astronaut": {
            "Title": "Woman Astronaut: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-astronaut-type-6_1f469-1f3ff-200d-1f680.png",
            "Gender": "Female",
            "OccupationName": "Astronaut",
            "SkinTone": "dark",
            "Location": "Milky Way",
            "SalaryMin": "65000",
            "SalaryMax": "150000"
        },
        "Female:light:Construction Worker": {
            "Title": "Woman Construction Worker: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-construction-worker-type-1-2_1f477-1f3fb-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Construction Worker",
            "SkinTone": "light",
            "Location": "Building Construction",
            "SalaryMin": "15000",
            "SalaryMax": "65000"
        },
        "Female:medium-light:Construction Worker": {
            "Title": "Woman Construction Worker: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-construction-worker-type-3_1f477-1f3fc-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Construction Worker",
            "SkinTone": "medium-light",
            "Location": "Building Construction",
            "SalaryMin": "15000",
            "SalaryMax": "65000"
        },
        "Female:medium:Construction Worker": {
            "Title": "Woman Construction Worker: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-construction-worker-type-4_1f477-1f3fd-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Construction Worker",
            "SkinTone": "medium",
            "Location": "Building Construction",
            "SalaryMin": "15000",
            "SalaryMax": "65000"
        },
        "Female:medium-dark:Construction Worker": {
            "Title": "Woman Construction Worker: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-construction-worker-type-5_1f477-1f3fe-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Construction Worker",
            "SkinTone": "medium-dark",
            "Location": "Building Construction",
            "SalaryMin": "15000",
            "SalaryMax": "65000"
        },
        "Female:dark:Construction Worker": {
            "Title": "Woman Construction Worker: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-construction-worker-type-6_1f477-1f3ff-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Construction Worker",
            "SkinTone": "dark",
            "Location": "Building Construction",
            "SalaryMin": "15000",
            "SalaryMax": "65000"
        },
        "Male:light:Construction Worker": {
            "Title": "Man Construction Worker: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-construction-worker-type-1-2_1f477-1f3fb-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Construction Worker",
            "SkinTone": "light",
            "Location": "Building Construction",
            "SalaryMin": "15000",
            "SalaryMax": "65000"
        },
        "Male:medium-light:Construction Worker": {
            "Title": "Man Construction Worker: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-construction-worker-type-3_1f477-1f3fc-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Construction Worker",
            "SkinTone": "medium-light",
            "Location": "Building Construction",
            "SalaryMin": "15000",
            "SalaryMax": "65000"
        },
        "Male:medium:Construction Worker": {
            "Title": "Man Construction Worker: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-construction-worker-type-4_1f477-1f3fd-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Construction Worker",
            "SkinTone": "medium",
            "Location": "Building Construction",
            "SalaryMin": "15000",
            "SalaryMax": "65000"
        },
        "Male:medium-dark:Construction Worker": {
            "Title": "Man Construction Worker: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-construction-worker-type-5_1f477-1f3fe-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Construction Worker",
            "SkinTone": "medium-dark",
            "Location": "Building Construction",
            "SalaryMin": "15000",
            "SalaryMax": "65000"
        },
        "Male:dark:Construction Worker": {
            "Title": "Man Construction Worker: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-construction-worker-type-6_1f477-1f3ff-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Construction Worker",
            "SkinTone": "dark",
            "Location": "Building Construction",
            "SalaryMin": "15000",
            "SalaryMax": "65000"
        },
        "Male:light:Cook": {
            "Title": "Man Cook: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-cook-type-1-2_1f468-1f3fb-200d-1f373.png",
            "Gender": "Male",
            "OccupationName": "Cook",
            "SkinTone": "light",
            "Location": "Department Store",
            "SalaryMin": "10000",
            "SalaryMax": "110000"
        },
        "Male:medium-light:Cook": {
            "Title": "Man Cook: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-cook-type-3_1f468-1f3fc-200d-1f373.png",
            "Gender": "Male",
            "OccupationName": "Cook",
            "SkinTone": "medium-light",
            "Location": "Department Store",
            "SalaryMin": "10000",
            "SalaryMax": "110000"
        },
        "Male:medium:Cook": {
            "Title": "Man Cook: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-cook-type-4_1f468-1f3fd-200d-1f373.png",
            "Gender": "Male",
            "OccupationName": "Cook",
            "SkinTone": "medium",
            "Location": "Department Store",
            "SalaryMin": "10000",
            "SalaryMax": "110000"
        },
        "Male:medium-dark:Cook": {
            "Title": "Man Cook: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-cook-type-5_1f468-1f3fe-200d-1f373.png",
            "Gender": "Male",
            "OccupationName": "Cook",
            "SkinTone": "medium-dark",
            "Location": "Department Store",
            "SalaryMin": "10000",
            "SalaryMax": "110000"
        },
        "Male:dark:Cook": {
            "Title": "Man Cook: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-cook-type-6_1f468-1f3ff-200d-1f373.png",
            "Gender": "Male",
            "OccupationName": "Cook",
            "SkinTone": "dark",
            "Location": "Department Store",
            "SalaryMin": "10000",
            "SalaryMax": "110000"
        },
        "Female:light:Cook": {
            "Title": "Woman Cook: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-cook-type-1-2_1f469-1f3fb-200d-1f373.png",
            "Gender": "Female",
            "OccupationName": "Cook",
            "SkinTone": "light",
            "Location": "Department Store",
            "SalaryMin": "10000",
            "SalaryMax": "110000"
        },
        "Female:medium-light:Cook": {
            "Title": "Woman Cook: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-cook-type-3_1f469-1f3fc-200d-1f373.png",
            "Gender": "Female",
            "OccupationName": "Cook",
            "SkinTone": "medium-light",
            "Location": "Department Store",
            "SalaryMin": "10000",
            "SalaryMax": "110000"
        },
        "Female:medium:Cook": {
            "Title": "Woman Cook: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-cook-type-4_1f469-1f3fd-200d-1f373.png",
            "Gender": "Female",
            "OccupationName": "Cook",
            "SkinTone": "medium",
            "Location": "Department Store",
            "SalaryMin": "10000",
            "SalaryMax": "110000"
        },
        "Female:medium-dark:Cook": {
            "Title": "Woman Cook: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-cook-type-5_1f469-1f3fe-200d-1f373.png",
            "Gender": "Female",
            "OccupationName": "Cook",
            "SkinTone": "medium-dark",
            "Location": "Department Store",
            "SalaryMin": "10000",
            "SalaryMax": "110000"
        },
        "Female:dark:Cook": {
            "Title": "Woman Cook: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-cook-type-6_1f469-1f3ff-200d-1f373.png",
            "Gender": "Female",
            "OccupationName": "Cook",
            "SkinTone": "dark",
            "Location": "Department Store",
            "SalaryMin": "10000",
            "SalaryMax": "110000"
        },
        "Male:light:Detective": {
            "Title": "Man Detective: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-sleuth-type-1-2_1f575-1f3fb-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Detective",
            "SkinTone": "light",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-light:Detective": {
            "Title": "Man Detective: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-sleuth-type-3_1f575-1f3fc-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Detective",
            "SkinTone": "medium-light",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium:Detective": {
            "Title": "Man Detective: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-sleuth-type-4_1f575-1f3fd-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Detective",
            "SkinTone": "medium",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-dark:Detective": {
            "Title": "Man Detective: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-sleuth-type-5_1f575-1f3fe-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Detective",
            "SkinTone": "medium-dark",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:dark:Detective": {
            "Title": "Man Detective: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-sleuth-type-6_1f575-1f3ff-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Detective",
            "SkinTone": "dark",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:light:Detective": {
            "Title": "Woman Detective: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-sleuth-type-1-2_1f575-1f3fb-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Detective",
            "SkinTone": "light",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-light:Detective": {
            "Title": "Woman Detective: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-sleuth-type-3_1f575-1f3fc-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Detective",
            "SkinTone": "medium-light",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium:Detective": {
            "Title": "Woman Detective: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-sleuth-type-4_1f575-1f3fd-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Detective",
            "SkinTone": "medium",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-dark:Detective": {
            "Title": "Woman Detective: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-sleuth-type-5_1f575-1f3fe-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Detective",
            "SkinTone": "medium-dark",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:dark:Detective": {
            "Title": "Woman Detective: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-sleuth-type-6_1f575-1f3ff-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Detective",
            "SkinTone": "dark",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:light:Factory Worker": {
            "Title": "Woman Factory Worker: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-factory-worker-type-1-2_1f469-1f3fb-200d-1f3ed.png",
            "Gender": "Female",
            "OccupationName": "Factory Worker",
            "SkinTone": "light",
            "Location": "Factory",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-light:Factory Worker": {
            "Title": "Woman Factory Worker: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-factory-worker-type-3_1f469-1f3fc-200d-1f3ed.png",
            "Gender": "Female",
            "OccupationName": "Factory Worker",
            "SkinTone": "medium-light",
            "Location": "Factory",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium:Factory Worker": {
            "Title": "Woman Factory Worker: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-factory-worker-type-4_1f469-1f3fd-200d-1f3ed.png",
            "Gender": "Female",
            "OccupationName": "Factory Worker",
            "SkinTone": "medium",
            "Location": "Factory",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-dark:Factory Worker": {
            "Title": "Woman Factory Worker: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-factory-worker-type-5_1f469-1f3fe-200d-1f3ed.png",
            "Gender": "Female",
            "OccupationName": "Factory Worker",
            "SkinTone": "medium-dark",
            "Location": "Factory",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:dark:Factory Worker": {
            "Title": "Woman Factory Worker: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-factory-worker-type-6_1f469-1f3ff-200d-1f3ed.png",
            "Gender": "Female",
            "OccupationName": "Factory Worker",
            "SkinTone": "dark",
            "Location": "Factory",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:light:Factory Worker": {
            "Title": "Man Factory Worker: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-factory-worker-type-1-2_1f468-1f3fb-200d-1f3ed.png",
            "Gender": "Male",
            "OccupationName": "Factory Worker",
            "SkinTone": "light",
            "Location": "Factory",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-light:Factory Worker": {
            "Title": "Man Factory Worker: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-factory-worker-type-3_1f468-1f3fc-200d-1f3ed.png",
            "Gender": "Male",
            "OccupationName": "Factory Worker",
            "SkinTone": "medium-light",
            "Location": "Factory",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium:Factory Worker": {
            "Title": "Man Factory Worker: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-factory-worker-type-4_1f468-1f3fd-200d-1f3ed.png",
            "Gender": "Male",
            "OccupationName": "Factory Worker",
            "SkinTone": "medium",
            "Location": "Factory",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-dark:Factory Worker": {
            "Title": "Man Factory Worker: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-factory-worker-type-5_1f468-1f3fe-200d-1f3ed.png",
            "Gender": "Male",
            "OccupationName": "Factory Worker",
            "SkinTone": "medium-dark",
            "Location": "Factory",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:dark:Factory Worker": {
            "Title": "Man Factory Worker: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-factory-worker-type-6_1f468-1f3ff-200d-1f3ed.png",
            "Gender": "Male",
            "OccupationName": "Factory Worker",
            "SkinTone": "dark",
            "Location": "Factory",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:light:Farmer": {
            "Title": "Man Farmer: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-farmer-type-1-2_1f468-1f3fb-200d-1f33e.png",
            "Gender": "Male",
            "OccupationName": "Farmer",
            "SkinTone": "light",
            "Location": "House With Garden",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-light:Farmer": {
            "Title": "Man Farmer: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-farmer-type-3_1f468-1f3fc-200d-1f33e.png",
            "Gender": "Male",
            "OccupationName": "Farmer",
            "SkinTone": "medium-light",
            "Location": "House With Garden",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium:Farmer": {
            "Title": "Man Farmer: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-farmer-type-4_1f468-1f3fd-200d-1f33e.png",
            "Gender": "Male",
            "OccupationName": "Farmer",
            "SkinTone": "medium",
            "Location": "House With Garden",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-dark:Farmer": {
            "Title": "Man Farmer: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-farmer-type-5_1f468-1f3fe-200d-1f33e.png",
            "Gender": "Male",
            "OccupationName": "Farmer",
            "SkinTone": "medium-dark",
            "Location": "House With Garden",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:dark:Farmer": {
            "Title": "Man Farmer: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-farmer-type-6_1f468-1f3ff-200d-1f33e.png",
            "Gender": "Male",
            "OccupationName": "Farmer",
            "SkinTone": "dark",
            "Location": "House With Garden",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:light:Farmer": {
            "Title": "Woman Farmer: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-farmer-type-1-2_1f469-1f3fb-200d-1f33e.png",
            "Gender": "Female",
            "OccupationName": "Farmer",
            "SkinTone": "light",
            "Location": "House With Garden",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-light:Farmer": {
            "Title": "Woman Farmer: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-farmer-type-3_1f469-1f3fc-200d-1f33e.png",
            "Gender": "Female",
            "OccupationName": "Farmer",
            "SkinTone": "medium-light",
            "Location": "House With Garden",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium:Farmer": {
            "Title": "Woman Farmer: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-farmer-type-4_1f469-1f3fd-200d-1f33e.png",
            "Gender": "Female",
            "OccupationName": "Farmer",
            "SkinTone": "medium",
            "Location": "House With Garden",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-dark:Farmer": {
            "Title": "Woman Farmer: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-farmer-type-5_1f469-1f3fe-200d-1f33e.png",
            "Gender": "Female",
            "OccupationName": "Farmer",
            "SkinTone": "medium-dark",
            "Location": "House With Garden",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:dark:Farmer": {
            "Title": "Woman Farmer: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-farmer-type-6_1f469-1f3ff-200d-1f33e.png",
            "Gender": "Female",
            "OccupationName": "Farmer",
            "SkinTone": "dark",
            "Location": "House With Garden",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:light:Firefighter": {
            "Title": "Man Firefighter: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-firefighter-type-1-2_1f468-1f3fb-200d-1f692.png",
            "Gender": "Male",
            "OccupationName": "Firefighter",
            "SkinTone": "light",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-light:Firefighter": {
            "Title": "Man Firefighter: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-firefighter-type-3_1f468-1f3fc-200d-1f692.png",
            "Gender": "Male",
            "OccupationName": "Firefighter",
            "SkinTone": "medium-light",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium:Firefighter": {
            "Title": "Man Firefighter: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-firefighter-type-4_1f468-1f3fd-200d-1f692.png",
            "Gender": "Male",
            "OccupationName": "Firefighter",
            "SkinTone": "medium",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-dark:Firefighter": {
            "Title": "Man Firefighter: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-firefighter-type-5_1f468-1f3fe-200d-1f692.png",
            "Gender": "Male",
            "OccupationName": "Firefighter",
            "SkinTone": "medium-dark",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:dark:Firefighter": {
            "Title": "Man Firefighter: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-firefighter-type-6_1f468-1f3ff-200d-1f692.png",
            "Gender": "Male",
            "OccupationName": "Firefighter",
            "SkinTone": "dark",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:light:Firefighter": {
            "Title": "Woman Firefighter: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-firefighter-type-1-2_1f469-1f3fb-200d-1f692.png",
            "Gender": "Female",
            "OccupationName": "Firefighter",
            "SkinTone": "light",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-light:Firefighter": {
            "Title": "Woman Firefighter: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-firefighter-type-3_1f469-1f3fc-200d-1f692.png",
            "Gender": "Female",
            "OccupationName": "Firefighter",
            "SkinTone": "medium-light",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium:Firefighter": {
            "Title": "Woman Firefighter: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-firefighter-type-4_1f469-1f3fd-200d-1f692.png",
            "Gender": "Female",
            "OccupationName": "Firefighter",
            "SkinTone": "medium",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-dark:Firefighter": {
            "Title": "Woman Firefighter: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-firefighter-type-5_1f469-1f3fe-200d-1f692.png",
            "Gender": "Female",
            "OccupationName": "Firefighter",
            "SkinTone": "medium-dark",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:dark:Firefighter": {
            "Title": "Woman Firefighter: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-firefighter-type-6_1f469-1f3ff-200d-1f692.png",
            "Gender": "Female",
            "OccupationName": "Firefighter",
            "SkinTone": "dark",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:light:Guard": {
            "Title": "Man Guard: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-guard-type-1-2_1f482-1f3fb-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Guard",
            "SkinTone": "light",
            "Location": "Castle",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-light:Guard": {
            "Title": "Man Guard: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-guard-type-3_1f482-1f3fc-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Guard",
            "SkinTone": "medium-light",
            "Location": "Castle",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium:Guard": {
            "Title": "Man Guard: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-guard-type-4_1f482-1f3fd-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Guard",
            "SkinTone": "medium",
            "Location": "Castle",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-dark:Guard": {
            "Title": "Man Guard: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-guard-type-5_1f482-1f3fe-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Guard",
            "SkinTone": "medium-dark",
            "Location": "Castle",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:dark:Guard": {
            "Title": "Man Guard: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-guard-type-6_1f482-1f3ff-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Guard",
            "SkinTone": "dark",
            "Location": "Castle",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:light:Guard": {
            "Title": "Woman Guard: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-guard-type-1-2_1f482-1f3fb-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Guard",
            "SkinTone": "light",
            "Location": "Castle",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-light:Guard": {
            "Title": "Woman Guard: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-guard-type-3_1f482-1f3fc-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Guard",
            "SkinTone": "medium-light",
            "Location": "Castle",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium:Guard": {
            "Title": "Woman Guard: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-guard-type-4_1f482-1f3fd-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Guard",
            "SkinTone": "medium",
            "Location": "Castle",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-dark:Guard": {
            "Title": "Woman Guard: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-guard-type-5_1f482-1f3fe-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Guard",
            "SkinTone": "medium-dark",
            "Location": "Castle",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:dark:Guard": {
            "Title": "Woman Guard: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-guard-type-6_1f482-1f3ff-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Guard",
            "SkinTone": "dark",
            "Location": "Castle",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:light:Health Worker": {
            "Title": "Woman Health Worker: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-health-worker-type-1-2_1f469-1f3fb-200d-2695-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Health Worker",
            "SkinTone": "light",
            "Location": "Hospital",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-light:Health Worker": {
            "Title": "Woman Health Worker: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-health-worker-type-3_1f469-1f3fc-200d-2695-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Health Worker",
            "SkinTone": "medium-light",
            "Location": "Hospital",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium:Health Worker": {
            "Title": "Woman Health Worker: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-health-worker-type-4_1f469-1f3fd-200d-2695-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Health Worker",
            "SkinTone": "medium",
            "Location": "Hospital",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-dark:Health Worker": {
            "Title": "Woman Health Worker: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-health-worker-type-5_1f469-1f3fe-200d-2695-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Health Worker",
            "SkinTone": "medium-dark",
            "Location": "Hospital",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:dark:Health Worker": {
            "Title": "Woman Health Worker: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-health-worker-type-6_1f469-1f3ff-200d-2695-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Health Worker",
            "SkinTone": "dark",
            "Location": "Hospital",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:light:Health Worker": {
            "Title": "Man Health Worker: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-health-worker-type-1-2_1f468-1f3fb-200d-2695-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Health Worker",
            "SkinTone": "light",
            "Location": "Hospital",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-light:Health Worker": {
            "Title": "Man Health Worker: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-health-worker-type-3_1f468-1f3fc-200d-2695-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Health Worker",
            "SkinTone": "medium-light",
            "Location": "Hospital",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium:Health Worker": {
            "Title": "Man Health Worker: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-health-worker-type-4_1f468-1f3fd-200d-2695-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Health Worker",
            "SkinTone": "medium",
            "Location": "Hospital",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-dark:Health Worker": {
            "Title": "Man Health Worker: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-health-worker-type-5_1f468-1f3fe-200d-2695-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Health Worker",
            "SkinTone": "medium-dark",
            "Location": "Hospital",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:dark:Health Worker": {
            "Title": "Man Health Worker: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-health-worker-type-6_1f468-1f3ff-200d-2695-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Health Worker",
            "SkinTone": "dark",
            "Location": "Hospital",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:light:Judge": {
            "Title": "Man Judge: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-judge-type-1-2_1f468-1f3fb-200d-2696-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Judge",
            "SkinTone": "light",
            "Location": "Classical Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-light:Judge": {
            "Title": "Man Judge: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-judge-type-3_1f468-1f3fc-200d-2696-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Judge",
            "SkinTone": "medium-light",
            "Location": "Classical Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium:Judge": {
            "Title": "Man Judge: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-judge-type-4_1f468-1f3fd-200d-2696-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Judge",
            "SkinTone": "medium",
            "Location": "Classical Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-dark:Judge": {
            "Title": "Man Judge: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-judge-type-5_1f468-1f3fe-200d-2696-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Judge",
            "SkinTone": "medium-dark",
            "Location": "Classical Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:dark:Judge": {
            "Title": "Man Judge: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-judge-type-6_1f468-1f3ff-200d-2696-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Judge",
            "SkinTone": "dark",
            "Location": "Classical Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:light:Judge": {
            "Title": "Woman Judge: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-judge-type-1-2_1f469-1f3fb-200d-2696-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Judge",
            "SkinTone": "light",
            "Location": "Classical Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-light:Judge": {
            "Title": "Woman Judge: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-judge-type-3_1f469-1f3fc-200d-2696-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Judge",
            "SkinTone": "medium-light",
            "Location": "Classical Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium:Judge": {
            "Title": "Woman Judge: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-judge-type-4_1f469-1f3fd-200d-2696-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Judge",
            "SkinTone": "medium",
            "Location": "Classical Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-dark:Judge": {
            "Title": "Woman Judge: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-judge-type-5_1f469-1f3fe-200d-2696-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Judge",
            "SkinTone": "medium-dark",
            "Location": "Classical Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:dark:Judge": {
            "Title": "Woman Judge: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-judge-type-6_1f469-1f3ff-200d-2696-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Judge",
            "SkinTone": "dark",
            "Location": "Classical Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:light:Mechanic": {
            "Title": "Man Mechanic: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-mechanic-type-1-2_1f468-1f3fb-200d-1f527.png",
            "Gender": "Male",
            "OccupationName": "Mechanic",
            "SkinTone": "light",
            "Location": "Convenience Store",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-light:Mechanic": {
            "Title": "Man Mechanic: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-mechanic-type-3_1f468-1f3fc-200d-1f527.png",
            "Gender": "Male",
            "OccupationName": "Mechanic",
            "SkinTone": "medium-light",
            "Location": "Convenience Store",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium:Mechanic": {
            "Title": "Man Mechanic: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-mechanic-type-4_1f468-1f3fd-200d-1f527.png",
            "Gender": "Male",
            "OccupationName": "Mechanic",
            "SkinTone": "medium",
            "Location": "Convenience Store",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-dark:Mechanic": {
            "Title": "Man Mechanic: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-mechanic-type-5_1f468-1f3fe-200d-1f527.png",
            "Gender": "Male",
            "OccupationName": "Mechanic",
            "SkinTone": "medium-dark",
            "Location": "Convenience Store",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:dark:Mechanic": {
            "Title": "Man Mechanic: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-mechanic-type-6_1f468-1f3ff-200d-1f527.png",
            "Gender": "Male",
            "OccupationName": "Mechanic",
            "SkinTone": "dark",
            "Location": "Convenience Store",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:light:Mechanic": {
            "Title": "Woman Mechanic: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-mechanic-type-1-2_1f469-1f3fb-200d-1f527.png",
            "Gender": "Female",
            "OccupationName": "Mechanic",
            "SkinTone": "light",
            "Location": "Convenience Store",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-light:Mechanic": {
            "Title": "Woman Mechanic: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-mechanic-type-3_1f469-1f3fc-200d-1f527.png",
            "Gender": "Female",
            "OccupationName": "Mechanic",
            "SkinTone": "medium-light",
            "Location": "Convenience Store",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium:Mechanic": {
            "Title": "Woman Mechanic: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-mechanic-type-4_1f469-1f3fd-200d-1f527.png",
            "Gender": "Female",
            "OccupationName": "Mechanic",
            "SkinTone": "medium",
            "Location": "Convenience Store",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-dark:Mechanic": {
            "Title": "Woman Mechanic: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-mechanic-type-5_1f469-1f3fe-200d-1f527.png",
            "Gender": "Female",
            "OccupationName": "Mechanic",
            "SkinTone": "medium-dark",
            "Location": "Convenience Store",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:dark:Mechanic": {
            "Title": "Woman Mechanic: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-mechanic-type-6_1f469-1f3ff-200d-1f527.png",
            "Gender": "Female",
            "OccupationName": "Mechanic",
            "SkinTone": "dark",
            "Location": "Convenience Store",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:light:Office Worker": {
            "Title": "Woman Office Worker: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-office-worker-type-1-2_1f469-1f3fb-200d-1f4bc.png",
            "Gender": "Female",
            "OccupationName": "Office Worker",
            "SkinTone": "light",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-light:Office Worker": {
            "Title": "Woman Office Worker: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-office-worker-type-3_1f469-1f3fc-200d-1f4bc.png",
            "Gender": "Female",
            "OccupationName": "Office Worker",
            "SkinTone": "medium-light",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium:Office Worker": {
            "Title": "Woman Office Worker: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-office-worker-type-4_1f469-1f3fd-200d-1f4bc.png",
            "Gender": "Female",
            "OccupationName": "Office Worker",
            "SkinTone": "medium",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-dark:Office Worker": {
            "Title": "Woman Office Worker: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-office-worker-type-5_1f469-1f3fe-200d-1f4bc.png",
            "Gender": "Female",
            "OccupationName": "Office Worker",
            "SkinTone": "medium-dark",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:dark:Office Worker": {
            "Title": "Woman Office Worker: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-office-worker-type-6_1f469-1f3ff-200d-1f4bc.png",
            "Gender": "Female",
            "OccupationName": "Office Worker",
            "SkinTone": "dark",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:light:Office Worker": {
            "Title": "Man Office Worker: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-office-worker-type-1-2_1f468-1f3fb-200d-1f4bc.png",
            "Gender": "Male",
            "OccupationName": "Office Worker",
            "SkinTone": "light",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-light:Office Worker": {
            "Title": "Man Office Worker: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-office-worker-type-3_1f468-1f3fc-200d-1f4bc.png",
            "Gender": "Male",
            "OccupationName": "Office Worker",
            "SkinTone": "medium-light",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium:Office Worker": {
            "Title": "Man Office Worker: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-office-worker-type-4_1f468-1f3fd-200d-1f4bc.png",
            "Gender": "Male",
            "OccupationName": "Office Worker",
            "SkinTone": "medium",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-dark:Office Worker": {
            "Title": "Man Office Worker: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-office-worker-type-5_1f468-1f3fe-200d-1f4bc.png",
            "Gender": "Male",
            "OccupationName": "Office Worker",
            "SkinTone": "medium-dark",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:dark:Office Worker": {
            "Title": "Man Office Worker: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-office-worker-type-6_1f468-1f3ff-200d-1f4bc.png",
            "Gender": "Male",
            "OccupationName": "Office Worker",
            "SkinTone": "dark",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:light:Pilot": {
            "Title": "Man Pilot: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-pilot-type-1-2_1f468-1f3fb-200d-2708-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Pilot",
            "SkinTone": "light",
            "Location": "Sunrise",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-light:Pilot": {
            "Title": "Man Pilot: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-pilot-type-3_1f468-1f3fc-200d-2708-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Pilot",
            "SkinTone": "medium-light",
            "Location": "Sunrise",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium:Pilot": {
            "Title": "Man Pilot: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-pilot-type-4_1f468-1f3fd-200d-2708-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Pilot",
            "SkinTone": "medium",
            "Location": "Sunrise",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-dark:Pilot": {
            "Title": "Man Pilot: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-pilot-type-5_1f468-1f3fe-200d-2708-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Pilot",
            "SkinTone": "medium-dark",
            "Location": "Sunrise",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:dark:Pilot": {
            "Title": "Man Pilot: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-pilot-type-6_1f468-1f3ff-200d-2708-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Pilot",
            "SkinTone": "dark",
            "Location": "Sunrise",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:light:Pilot": {
            "Title": "Woman Pilot: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-pilot-type-1-2_1f469-1f3fb-200d-2708-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Pilot",
            "SkinTone": "light",
            "Location": "Sunrise",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-light:Pilot": {
            "Title": "Woman Pilot: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-pilot-type-3_1f469-1f3fc-200d-2708-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Pilot",
            "SkinTone": "medium-light",
            "Location": "Sunrise",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium:Pilot": {
            "Title": "Woman Pilot: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-pilot-type-4_1f469-1f3fd-200d-2708-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Pilot",
            "SkinTone": "medium",
            "Location": "Sunrise",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-dark:Pilot": {
            "Title": "Woman Pilot: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-pilot-type-5_1f469-1f3fe-200d-2708-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Pilot",
            "SkinTone": "medium-dark",
            "Location": "Sunrise",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:dark:Pilot": {
            "Title": "Woman Pilot: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-pilot-type-6_1f469-1f3ff-200d-2708-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Pilot",
            "SkinTone": "dark",
            "Location": "Sunrise",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:light:Police Officer": {
            "Title": "Woman Police Officer: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-police-officer-type-1-2_1f46e-1f3fb-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Police Officer",
            "SkinTone": "light",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-light:Police Officer": {
            "Title": "Woman Police Officer: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-police-officer-type-3_1f46e-1f3fc-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Police Officer",
            "SkinTone": "medium-light",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium:Police Officer": {
            "Title": "Woman Police Officer: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-police-officer-type-4_1f46e-1f3fd-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Police Officer",
            "SkinTone": "medium",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-dark:Police Officer": {
            "Title": "Woman Police Officer: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-police-officer-type-5_1f46e-1f3fe-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Police Officer",
            "SkinTone": "medium-dark",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:dark:Police Officer": {
            "Title": "Woman Police Officer: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-police-officer-type-6_1f46e-1f3ff-200d-2640-fe0f.png",
            "Gender": "Female",
            "OccupationName": "Police Officer",
            "SkinTone": "dark",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:light:Police Officer": {
            "Title": "Man Police Officer: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-police-officer-type-1-2_1f46e-1f3fb-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Police Officer",
            "SkinTone": "light",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-light:Police Officer": {
            "Title": "Man Police Officer: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-police-officer-type-3_1f46e-1f3fc-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Police Officer",
            "SkinTone": "medium-light",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium:Police Officer": {
            "Title": "Man Police Officer: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-police-officer-type-4_1f46e-1f3fd-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Police Officer",
            "SkinTone": "medium",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-dark:Police Officer": {
            "Title": "Man Police Officer: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-police-officer-type-5_1f46e-1f3fe-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Police Officer",
            "SkinTone": "medium-dark",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:dark:Police Officer": {
            "Title": "Man Police Officer: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-police-officer-type-6_1f46e-1f3ff-200d-2642-fe0f.png",
            "Gender": "Male",
            "OccupationName": "Police Officer",
            "SkinTone": "dark",
            "Location": "Station",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:light:Scientist": {
            "Title": "Man Scientist: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-scientist-type-1-2_1f468-1f3fb-200d-1f52c.png",
            "Gender": "Male",
            "OccupationName": "Scientist",
            "SkinTone": "light",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-light:Scientist": {
            "Title": "Man Scientist: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-scientist-type-3_1f468-1f3fc-200d-1f52c.png",
            "Gender": "Male",
            "OccupationName": "Scientist",
            "SkinTone": "medium-light",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium:Scientist": {
            "Title": "Man Scientist: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-scientist-type-4_1f468-1f3fd-200d-1f52c.png",
            "Gender": "Male",
            "OccupationName": "Scientist",
            "SkinTone": "medium",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-dark:Scientist": {
            "Title": "Man Scientist: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-scientist-type-5_1f468-1f3fe-200d-1f52c.png",
            "Gender": "Male",
            "OccupationName": "Scientist",
            "SkinTone": "medium-dark",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:dark:Scientist": {
            "Title": "Man Scientist: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-scientist-type-6_1f468-1f3ff-200d-1f52c.png",
            "Gender": "Male",
            "OccupationName": "Scientist",
            "SkinTone": "dark",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:light:Scientist": {
            "Title": "Woman Scientist: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-scientist-type-1-2_1f469-1f3fb-200d-1f52c.png",
            "Gender": "Female",
            "OccupationName": "Scientist",
            "SkinTone": "light",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-light:Scientist": {
            "Title": "Woman Scientist: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-scientist-type-3_1f469-1f3fc-200d-1f52c.png",
            "Gender": "Female",
            "OccupationName": "Scientist",
            "SkinTone": "medium-light",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium:Scientist": {
            "Title": "Woman Scientist: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-scientist-type-4_1f469-1f3fd-200d-1f52c.png",
            "Gender": "Female",
            "OccupationName": "Scientist",
            "SkinTone": "medium",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-dark:Scientist": {
            "Title": "Woman Scientist: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-scientist-type-5_1f469-1f3fe-200d-1f52c.png",
            "Gender": "Female",
            "OccupationName": "Scientist",
            "SkinTone": "medium-dark",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:dark:Scientist": {
            "Title": "Woman Scientist: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-scientist-type-6_1f469-1f3ff-200d-1f52c.png",
            "Gender": "Female",
            "OccupationName": "Scientist",
            "SkinTone": "dark",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:light:Singer": {
            "Title": "Man Singer: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-singer-type-1-2_1f468-1f3fb-200d-1f3a4.png",
            "Gender": "Male",
            "OccupationName": "Singer",
            "SkinTone": "light",
            "Location": "Stadium",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-light:Singer": {
            "Title": "Man Singer: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-singer-type-3_1f468-1f3fc-200d-1f3a4.png",
            "Gender": "Male",
            "OccupationName": "Singer",
            "SkinTone": "medium-light",
            "Location": "Stadium",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium:Singer": {
            "Title": "Man Singer: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-singer-type-4_1f468-1f3fd-200d-1f3a4.png",
            "Gender": "Male",
            "OccupationName": "Singer",
            "SkinTone": "medium",
            "Location": "Stadium",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-dark:Singer": {
            "Title": "Man Singer: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-singer-type-5_1f468-1f3fe-200d-1f3a4.png",
            "Gender": "Male",
            "OccupationName": "Singer",
            "SkinTone": "medium-dark",
            "Location": "Stadium",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:dark:Singer": {
            "Title": "Man Singer: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-singer-type-6_1f468-1f3ff-200d-1f3a4.png",
            "Gender": "Male",
            "OccupationName": "Singer",
            "SkinTone": "dark",
            "Location": "Stadium",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:light:Singer": {
            "Title": "Woman Singer: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-singer-type-1-2_1f469-1f3fb-200d-1f3a4.png",
            "Gender": "Female",
            "OccupationName": "Singer",
            "SkinTone": "light",
            "Location": "Stadium",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-light:Singer": {
            "Title": "Woman Singer: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-singer-type-3_1f469-1f3fc-200d-1f3a4.png",
            "Gender": "Female",
            "OccupationName": "Singer",
            "SkinTone": "medium-light",
            "Location": "Stadium",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium:Singer": {
            "Title": "Woman Singer: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-singer-type-4_1f469-1f3fd-200d-1f3a4.png",
            "Gender": "Female",
            "OccupationName": "Singer",
            "SkinTone": "medium",
            "Location": "Stadium",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-dark:Singer": {
            "Title": "Woman Singer: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-singer-type-5_1f469-1f3fe-200d-1f3a4.png",
            "Gender": "Female",
            "OccupationName": "Singer",
            "SkinTone": "medium-dark",
            "Location": "Stadium",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:dark:Singer": {
            "Title": "Woman Singer: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-singer-type-6_1f469-1f3ff-200d-1f3a4.png",
            "Gender": "Female",
            "OccupationName": "Singer",
            "SkinTone": "dark",
            "Location": "Stadium",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:light:Teacher": {
            "Title": "Man Teacher: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-teacher-type-1-2_1f468-1f3fb-200d-1f3eb.png",
            "Gender": "Male",
            "OccupationName": "Teacher",
            "SkinTone": "light",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-light:Teacher": {
            "Title": "Man Teacher: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-teacher-type-3_1f468-1f3fc-200d-1f3eb.png",
            "Gender": "Male",
            "OccupationName": "Teacher",
            "SkinTone": "medium-light",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium:Teacher": {
            "Title": "Man Teacher: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-teacher-type-4_1f468-1f3fd-200d-1f3eb.png",
            "Gender": "Male",
            "OccupationName": "Teacher",
            "SkinTone": "medium",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-dark:Teacher": {
            "Title": "Man Teacher: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-teacher-type-5_1f468-1f3fe-200d-1f3eb.png",
            "Gender": "Male",
            "OccupationName": "Teacher",
            "SkinTone": "medium-dark",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:dark:Teacher": {
            "Title": "Man Teacher: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-teacher-type-6_1f468-1f3ff-200d-1f3eb.png",
            "Gender": "Male",
            "OccupationName": "Teacher",
            "SkinTone": "dark",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:light:Teacher": {
            "Title": "Woman Teacher: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-teacher-type-1-2_1f469-1f3fb-200d-1f3eb.png",
            "Gender": "Female",
            "OccupationName": "Teacher",
            "SkinTone": "light",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-light:Teacher": {
            "Title": "Woman Teacher: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-teacher-type-3_1f469-1f3fc-200d-1f3eb.png",
            "Gender": "Female",
            "OccupationName": "Teacher",
            "SkinTone": "medium-light",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium:Teacher": {
            "Title": "Woman Teacher: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-teacher-type-4_1f469-1f3fd-200d-1f3eb.png",
            "Gender": "Female",
            "OccupationName": "Teacher",
            "SkinTone": "medium",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-dark:Teacher": {
            "Title": "Woman Teacher: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-teacher-type-5_1f469-1f3fe-200d-1f3eb.png",
            "Gender": "Female",
            "OccupationName": "Teacher",
            "SkinTone": "medium-dark",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:dark:Teacher": {
            "Title": "Woman Teacher: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-teacher-type-6_1f469-1f3ff-200d-1f3eb.png",
            "Gender": "Female",
            "OccupationName": "Teacher",
            "SkinTone": "dark",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:light:Technologist": {
            "Title": "Man Technologist: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-technologist-type-1-2_1f468-1f3fb-200d-1f4bb.png",
            "Gender": "Male",
            "OccupationName": "Technologist",
            "SkinTone": "light",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-light:Technologist": {
            "Title": "Man Technologist: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-technologist-type-3_1f468-1f3fc-200d-1f4bb.png",
            "Gender": "Male",
            "OccupationName": "Technologist",
            "SkinTone": "medium-light",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium:Technologist": {
            "Title": "Man Technologist: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-technologist-type-4_1f468-1f3fd-200d-1f4bb.png",
            "Gender": "Male",
            "OccupationName": "Technologist",
            "SkinTone": "medium",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-dark:Technologist": {
            "Title": "Man Technologist: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-technologist-type-5_1f468-1f3fe-200d-1f4bb.png",
            "Gender": "Male",
            "OccupationName": "Technologist",
            "SkinTone": "medium-dark",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:dark:Technologist": {
            "Title": "Man Technologist: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-technologist-type-6_1f468-1f3ff-200d-1f4bb.png",
            "Gender": "Male",
            "OccupationName": "Technologist",
            "SkinTone": "dark",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:light:Technologist": {
            "Title": "Woman Technologist: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-technologist-type-1-2_1f469-1f3fb-200d-1f4bb.png",
            "Gender": "Female",
            "OccupationName": "Technologist",
            "SkinTone": "light",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-light:Technologist": {
            "Title": "Woman Technologist: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-technologist-type-3_1f469-1f3fc-200d-1f4bb.png",
            "Gender": "Female",
            "OccupationName": "Technologist",
            "SkinTone": "medium-light",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium:Technologist": {
            "Title": "Woman Technologist: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-technologist-type-4_1f469-1f3fd-200d-1f4bb.png",
            "Gender": "Female",
            "OccupationName": "Technologist",
            "SkinTone": "medium",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-dark:Technologist": {
            "Title": "Woman Technologist: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-technologist-type-5_1f469-1f3fe-200d-1f4bb.png",
            "Gender": "Female",
            "OccupationName": "Technologist",
            "SkinTone": "medium-dark",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:dark:Technologist": {
            "Title": "Woman Technologist: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-technologist-type-6_1f469-1f3ff-200d-1f4bb.png",
            "Gender": "Female",
            "OccupationName": "Technologist",
            "SkinTone": "dark",
            "Location": "Office Building",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:light:Student": {
            "Title": "Man Student: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-student-type-1-2_1f468-1f3fb-200d-1f393.png",
            "Gender": "Male",
            "OccupationName": "Student",
            "SkinTone": "light",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-light:Student": {
            "Title": "Man Student: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-student-type-3_1f468-1f3fc-200d-1f393.png",
            "Gender": "Male",
            "OccupationName": "Student",
            "SkinTone": "medium-light",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium:Student": {
            "Title": "Man Student: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-student-type-4_1f468-1f3fd-200d-1f393.png",
            "Gender": "Male",
            "OccupationName": "Student",
            "SkinTone": "medium",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-dark:Student": {
            "Title": "Man Student: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-student-type-5_1f468-1f3fe-200d-1f393.png",
            "Gender": "Male",
            "OccupationName": "Student",
            "SkinTone": "medium-dark",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:dark:Student": {
            "Title": "Man Student: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/male-student-type-6_1f468-1f3ff-200d-1f393.png",
            "Gender": "Male",
            "OccupationName": "Student",
            "SkinTone": "dark",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:light:Student": {
            "Title": "Woman Student: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-student-type-1-2_1f469-1f3fb-200d-1f393.png",
            "Gender": "Female",
            "OccupationName": "Student",
            "SkinTone": "light",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-light:Student": {
            "Title": "Woman Student: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-student-type-3_1f469-1f3fc-200d-1f393.png",
            "Gender": "Female",
            "OccupationName": "Student",
            "SkinTone": "medium-light",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium:Student": {
            "Title": "Woman Student: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-student-type-4_1f469-1f3fd-200d-1f393.png",
            "Gender": "Female",
            "OccupationName": "Student",
            "SkinTone": "medium",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-dark:Student": {
            "Title": "Woman Student: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-student-type-5_1f469-1f3fe-200d-1f393.png",
            "Gender": "Female",
            "OccupationName": "Student",
            "SkinTone": "medium-dark",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:dark:Student": {
            "Title": "Woman Student: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/158/female-student-type-6_1f469-1f3ff-200d-1f393.png",
            "Gender": "Female",
            "OccupationName": "Student",
            "SkinTone": "dark",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:light:Childcare": {
            "Title": "Family - Man: Light Skin Tone, Girl: Light Skin Tone, Boy: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/family-man-light-skin-tone-girl-light-skin-tone-boy-light-skin-tone_1f468-1f3fb-200d-1f467-1f3fb-200d-1f466-1f3fb.png",
            "Gender": "Male",
            "OccupationName": "Childcare",
            "SkinTone": "light",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-light:Childcare": {
            "Title": "Family - Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/family-man-medium-light-skin-tone-girl-medium-light-skin-tone-boy-medium-light-skin-tone_1f468-1f3fc-200d-1f467-1f3fc-200d-1f466-1f3fc.png",
            "Gender": "Male",
            "OccupationName": "Childcare",
            "SkinTone": "medium-light",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium:Childcare": {
            "Title": "Family - Man: Medium Skin Tone, Girl: Medium Skin Tone, Boy: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/family-man-medium-skin-tone-girl-medium-skin-tone-boy-medium-skin-tone_1f468-1f3fd-200d-1f467-1f3fd-200d-1f466-1f3fd.png",
            "Gender": "Male",
            "OccupationName": "Childcare",
            "SkinTone": "medium",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:medium-dark:Childcare": {
            "Title": "Family - Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/family-man-medium-dark-skin-tone-girl-medium-dark-skin-tone-boy-medium-dark-skin-tone_1f468-1f3fe-200d-1f467-1f3fe-200d-1f466-1f3fe.png",
            "Gender": "Male",
            "OccupationName": "Childcare",
            "SkinTone": "medium-dark",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Male:dark:Childcare": {
            "Title": "Family - Man: Dark Skin Tone, Girl: Dark Skin Tone, Boy: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/family-man-dark-skin-tone-girl-dark-skin-tone-boy-dark-skin-tone_1f468-1f3ff-200d-1f467-1f3ff-200d-1f466-1f3ff.png",
            "Gender": "Male",
            "OccupationName": "Childcare",
            "SkinTone": "dark",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:light:Childcare": {
            "Title": "Family - Woman: Light Skin Tone, Girl: Light Skin Tone, Boy: Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/family-woman-light-skin-tone-girl-light-skin-tone-boy-light-skin-tone_1f469-1f3fb-200d-1f467-1f3fb-200d-1f466-1f3fb.png",
            "Gender": "Female",
            "OccupationName": "Childcare",
            "SkinTone": "light",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-light:Childcare": {
            "Title": "Family - Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/family-woman-medium-light-skin-tone-girl-medium-light-skin-tone-boy-medium-light-skin-tone_1f469-1f3fc-200d-1f467-1f3fc-200d-1f466-1f3fc.png",
            "Gender": "Female",
            "OccupationName": "Childcare",
            "SkinTone": "medium-light",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium:Childcare": {
            "Title": "Family - Woman: Medium Skin Tone, Girl: Medium Skin Tone, Boy: Medium Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/family-woman-medium-skin-tone-girl-medium-skin-tone-boy-medium-skin-tone_1f469-1f3fd-200d-1f467-1f3fd-200d-1f466-1f3fd.png",
            "Gender": "Female",
            "OccupationName": "Childcare",
            "SkinTone": "medium",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:medium-dark:Childcare": {
            "Title": "Family - Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/family-woman-medium-dark-skin-tone-girl-medium-dark-skin-tone-boy-medium-dark-skin-tone_1f469-1f3fe-200d-1f467-1f3fe-200d-1f466-1f3fe.png",
            "Gender": "Female",
            "OccupationName": "Childcare",
            "SkinTone": "medium-dark",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        },
        "Female:dark:Childcare": {
            "Title": "Family - Woman: Dark Skin Tone, Girl: Dark Skin Tone, Boy: Dark Skin Tone",
            "Source": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/230/family-woman-dark-skin-tone-girl-dark-skin-tone-boy-dark-skin-tone_1f469-1f3ff-200d-1f467-1f3ff-200d-1f466-1f3ff.png",
            "Gender": "Female",
            "OccupationName": "Childcare",
            "SkinTone": "dark",
            "Location": "School",
            "SalaryMin": "10000",
            "SalaryMax": "70000"
        }
    }

    job_titles = {
        "Accountant": "Office Worker",
        "Actor": "Actor",
        "Administrator": "Technologist",
        "Artist": "Artist",
        "Athletic coach": "Teacher",
        "Banker": "Technologist",
        "Bookkeeper": "Teacher",
        "Business analyst": "Office Worker",
        "Business manager": "Office Worker",
        "Carpentry": "Mechanic",
        "Chef": "Cook",
        "Child care provider": "Childcare",
        "Childcare": "Childcare",
        "Company CEO or manager": "Office Worker",
        "Composer or musician": "Singer",
        "Computer programming": "Technologist",
        "Computer support technician": "Technologist",
        "Counseling": "Counselor",
        "Counselor": "Counselor",
        "Dentist": "Health Worker",
        "Designer": "Artist",
        "Detectives": "Detective",
        "Doctor": "Health Worker",
        "Electrician": "Mechanic",
        "Engineer": "Factory Worker",
        "Engineering": "Factory Worker",
        "Entrepreneur": "Office Worker",
        "Fashion designer": "Artist",
        "Firefighter": "Firefighter",
        "Forensic science": "Scientist",
        "Forest ranger": "Police Officer",
        "Graphic Designer": "Office Worker",
        "Human resources manager": "Office Worker",
        "Human resources specialist": "Office Worker",
        "Inventor": "Scientist",
        "Journalist": "Detective",
        "Judge": "Judge",
        "Law enforcement": "Police Officer",
        "Lawyer": "Office Worker",
        "Librarian": "Teacher",
        "Manager": "Office Worker",
        "Marketer": "Office Worker",
        "Mathematician": "Teacher",
        "Mechanics": "Mechanic",
        "Military": "Pilot",
        "Musician": "Singer",
        "Naturalist": "Farmer",
        "Nurse": "Health Worker",
        "Nursing": "Health Worker",
        "Nutritionist": "Health Worker",
        "Office Manager": "Office Worker",
        "Paralegal": "Office Worker",
        "Paramedic": "Health Worker",
        "Pediatrician": "Health Worker",
        "Photographer": "Detective",
        "Physical Therapist": "Health Worker",
        "Physician": "Health Worker",
        "Pilot": "Pilot",
        "Police officer": "Police Officer",
        "Police officers": "Police Officer",
        "Politician": "Office Worker",
        "Psychiatrist": "Health Worker",
        "Psychologist": "Health Worker",
        "Receptionist": "Technologist",
        "Religious worker": "Pilot",
        "Sales agent": "Office Worker",
        "Sales representative": "Office Worker",
        "School administrator": "Teacher",
        "Scientist": "Scientist",
        "Social work": "Teacher",
        "Social Worker": "Teacher",
        "Software developer": "Technologist",
        "Software engineer": "Technologist",
        "Teacher": "Teacher",
        "Teaching": "Teacher",
        "TV Anchor/Reporter": "Office Worker",
        "University professor": "Teacher",
        "Veterinarian": "Health Worker",
        "Video game designer": "Technologist",
        "Writer": "Technologist"
    }

    personality_types = {
        "INTJ": {
            "Type": [
                "Introversion",
                "Intuition",
                "Thinking",
                "Judging"
            ],
            "Name": "The Architect",
            "AltName": "The Architect",
            "Class": "fas fa-shapes",
            "BGColor": "#606060",
            "FTColor": "wheat",
            "Description": "Imaginative and strategic thinkers, with a plan for everything.",
            "Dominant": "Introverted Intuition",
            "Auxiliary": "Extraverted Thinking",
            "Tertiary": "Introverted Feeling",
            "Inferior": "Extraverted Sensing",
            "KeyCharacteristics": [
                "Intjs Tend To Be Introverted And Prefer To Work Alone.",
                "Intjs Look At The Big Picture And Like To Focus On Abstract Information Rather Than Concrete Details.",
                "Intjs Place Greater Emphasis On Logic And Objective Information Rather Than Subjective Emotions.",
                "Intjs Like Their World To Feel Controlled And Ordered So They Prefer To Make Plans Well In Advance."
            ],
            "Strengths": [
                "Enjoys Theoretical And Abstract Concepts",
                "High Expectations",
                "Good At Listening",
                "Takes Criticism Well",
                "Self-Confident And Hard-Working"
            ],
            "Weaknesses": [
                "Can Be Overly Analytical And Judgmental",
                "Very Perfectionistic",
                "Dislikes Talking About Emotions",
                "Sometimes Seems Callous Or Insensitive"
            ],
            "KnownCelbrities": [
                "Thomas Jefferson, U.S. President",
                "C.S. Lewis, Author",
                "Arnold Schwarzenegger, Actor & Politician",
                "Gandalf, The Lord Of The Rings",
                "Lance Armstrong, Cyclist"
            ],
            "Careers": [
                "Scientist",
                "Mathematician",
                "Engineer",
                "Dentist",
                "Doctor",
                "Teacher",
                "Judge",
                "Lawyer"
            ]
        },
        "INTP": {
            "Type": [
                "Introversion",
                "Intuition",
                "Thinking",
                "Perceiving"
            ],
            "Name": "The Thinker",
            "AltName": "The Thinker",
            "Class": "fas fa-brain",
            "BGColor": "#e52a47",
            "FTColor": "wheat",
            "Description": "Innovative inventors with an unquenchable thirst for knowledge.",
            "Dominant": "Introverted Thinking",
            "Auxiliary": "Extraverted Intuition",
            "Tertiary": "Introverted Sensing",
            "Inferior": "Extraverted Feeling",
            "KeyCharacteristics": [
                "Intps Are Quiet, Reserved, And Thoughtful. As Introverts, They Prefer To Socialize With A Small Group Of Close Friends With Whom They Share Common Interests And Connections.",
                "They Enjoy Thinking About Theoretical Concepts And Tend To Value Intellect Over Emotion. Intps Are Logical And Base Decisions On Objective Information Rather Than Subjective Feelings.",
                "When Analyzing Data And Making Decisions, They Are Highly Logical And Objective.",
                "Tends To Be Flexible And Good At Thinking Outside Of The Box.",
                "People With This Personality Type Think About The Big Picture Rather Than Focusing On Every Tiny Detail.",
                "Intps Like To Keep Their Options Open And Feel Limited By Structure And Planning."
            ],
            "Strengths": [
                "Logical And Objective",
                "Abstract Thinker",
                "Independent",
                "Loyal And Affectionate With Loved Ones"
            ],
            "Weaknesses": [
                "Difficult To Get To Know",
                "Can Be Insensitive",
                "Prone To Self-Doubt",
                "Struggles To Follow Rules",
                "Has Trouble Expressing Feelings"
            ],
            "KnownCelbrities": [
                "Albert Einstein, Scientist",
                "Dwight D. Eisenhower, U.S. President",
                "Carl Jung, Psychoanalyst",
                "Tiger Woods, Golfer",
                "Sheldon Cooper, The Big Bang Theory"
            ],
            "Careers": [
                "Scientist",
                "Mathematician",
                "Engineer",
                "Dentist",
                "Doctor",
                "Teacher",
                "Judge",
                "Lawyer"
            ]
        },
        "ENTJ": {
            "Type": [
                "Extroversion",
                "Intuition",
                "Thinking",
                "Judging"
            ],
            "Name": "The Commander",
            "AltName": "The Commander",
            "Class": "fas fa-chess-king",
            "BGColor": "#99892d",
            "FTColor": "wheat",
            "Description": "Bold, imaginative and strong-willed leaders, always finding a way or making one.",
            "Dominant": "Extraverted Thinking",
            "Auxiliary": "Introverted Intuition",
            "Tertiary": "Extraverted Sensing",
            "Inferior": "Introverted Feeling",
            "KeyCharacteristics": [
                "People With This Personality Type Enjoy Spending Time With Other People. They Have Strong Verbal Skills And Interacting With Others Helps Them Feel Energized.",
                "Entj Types Prefer To Think About The Future Rather Than Focus On The Here-And-Now. They Usually Find Abstract And Theoretical Information More Interesting Than Concrete Details.",
                "When Making Decisions, Entjs Place A Greater Emphasis On Objective And Logical Information. Personal Feeling And The Emotions Of Others Tend Not To Factor Much Into Their Choices.2Introduction To Type In College. Cpp; 1993.\\Ufeff",
                "Entjs Are Planners. Making Decisions And Having A Schedule Or Course Of Action Planned Out Gives Them A Sense Of Predictability And Control.",
                "They Are Highly Rational, Good At Spotting Problems, And Excel At Taking Charge. These Tendencies Make Them Natural Leaders Who Are Focused On Efficiently Solving Problems.",
                "One Myth About Entjs Is That They Are Cold And Ruthless. While They Are Not Necessarily Good With Emotions, This Does Not Mean That They Are Intentionally Cruel. They Are Prone To Hiding Their Own Emotions And Sentimentality, Viewing It As A Weakness That Should Not Be Made Known To Others.",
                "This Is An Entj Preferred Functioned And Is Expressed Through The Way They Make Decisions And Judgments.",
                "Entjs Have A Tendency To Speak First Without Listening, Making Snap Judgments Before Really Taking In All The Information Pertaining To A Situation.",
                "While They Tend To Make Snap Judgments, They Are Also Very Rational And Objective. They Are Focused On Imposing Order And Standards On The World Around Them. Setting Measurable Goals Is Important.",
                "People With This Personality Type Are Future-Focused And Always Consider The Possibilities When Approaching A Decision.",
                "Entjs Are Forward-Thinking And Are Not Afraid Of Change. They Trust Their Instincts, Although They May Have A Tendency To Regret Jumping To Conclusions So Quickly.",
                "This Cognitive Function Gives Entjs An Appetite For Adventure. They Enjoy Novel Experiences And May Sometimes Engage In Thrill-Seeking Behaviors.",
                "Because Their Outward Sensory Focus, They Also Have An Appreciation For Beautiful Things In Life. They Often Enjoy Surrounding Themselves With Things That They Find Attractive Or Interesting.",
                "Introverted Feeling Is Centered On Internal Feelings And Values. Emotions Can Be\\U00A0Difficult Area For Entjs, And They Often Lack An Understanding Of How This Part Of Their Personality Contributes To Their Decision-Making Process.",
                "When This Aspect Of Personality Is Weak, Entjs May Find Themselves Feeling Uncomfortable Or Awkward In Settings Where Some Type Of Emotional Response Is Called For."
            ],
            "Strengths": [
                "Strong Leadership Skills",
                "Self-Assured",
                "Well-Organized",
                "Good At Making Decisions",
                "Assertive And Outspoken",
                "Strong Communication Skills"
            ],
            "Weaknesses": [
                "Impatient",
                "Stubborn",
                "Insensitive",
                "Aggressive",
                "Intolerant"
            ],
            "KnownCelbrities": [
                "Franklin D. Roosevelt, U.S. President",
                "Bill Gates, Microsoft Founder",
                "Vince Lombardi, Football Coach",
                "Carl Sagan, Astronomer",
                "Lex Luthor, Superman Character"
            ],
            "Careers": [
                "Human Resources Manager",
                "Company Ceo Or Manager",
                "Lawyer",
                "Scientist",
                "Software Developer",
                "Business Analyst",
                "Entrepreneur",
                "University Professor"
            ]
        },
        "ENTP": {
            "Type": [
                "Extroversion",
                "Intuition",
                "Thinking",
                "Perceiving"
            ],
            "Name": "Debater",
            "AltName": "The Debater",
            "Class": "fas fa-bullhorn",
            "BGColor": "#213164",
            "FTColor": "wheat",
            "Description": "Smart and curious thinkers who cannot resist an intellectual challenge.",
            "Dominant": "Extraverted Intuition",
            "Auxiliary": "Introverted Thinking",
            "Tertiary": "Extraverted Feeling",
            "Inferior": "Introverted Sensing",
            "KeyCharacteristics": [
                "Entps Enjoy Interacting With A Wide Variety Of People. They Are Great Conversationalists And Love To Engage Other People In Debates.",
                "They Are More Focused On The Future Rather Than On Immediate Details. They May Start Projects And Never Finish Them Because They Are So Focused On The Big Picture Rather Than The Present Needs.",
                "Entps Enjoy Being Around Other People, Particularly If They Are Able To Engage In A Conversation Or Debate About Something In Which They Are Interested. They Are Usually Fairly Laid-Back And Easy To Get Along With. However, They Can Sometimes Get So Wrapped Up In Their Ideas Or Plans That They Lose Sight Of Their Close Relationships.",
                "They Tend To Reserve Judgment. Instead Of Making A Decision Or Committing To A Course Of Action, They Would Prefer To Wait And See What Happens.",
                "Entps Are Immensely Curious And Focused On Understanding The World Around Them. They Are Constantly Absorbing New Information And Ideas And Quickly Arriving At Conclusions. They Are Able To Understand New Things Quite Quickly.",
                "One Common Myth About Entps Is That They Love To Argue Simply For The Sake Of Arguing. While People With This Personality Type Are Often Willing To Play The Devil'S Advocate At Times, They Enjoy Debates As A Way Of Exploring A Topic, Learning What Other People Believe, And Helping Others See The Other Side Of The Story.",
                "Entps Tend To Take In Information Quickly And Are Very Open-Minded.",
                "Once They Have Gathered This Information, They Spend Time Making Connections Between Various Complex And Interwoven Relationships.",
                "They Are Good At Spotting Connections That Others Might Overlook And Tend To Be Focused On Possibilities.",
                "They Have Entrepreneurial Minds And Are Always Coming Up With New And Exciting Ideas.",
                "This Cognitive Function Is Expressed In The Entps Thinking Process. People With This Type Of Personality Are More Focused On Taking In Information About The World Around Them. When They Do Use This Information To Reach Conclusions, They Tend To Be Very Logical.",
                "Entps Are Logical And Objective. When\\U00A0Making Decisions, They Place A Greater Weight On Rational Evidence Instead Of Subjective, Emotional Information.",
                "This Function Works To Help The Entp Understand All The Information That Comes In Through The Extraverted Intuition Function. This Involves Imposing Logic And Order To Help Make Sense Of Many Disparate Ideas And Pieces Of Information. Entps Don'T Want To Just Understand That Something Works - They Want To Understand The Why And How Behind How Things Function.",
                "As A Tertiary Function, This Aspect Of Personality May Not Be As Well-Developed Or Prominent.",
                "When Developed, Entps Can Be Social Charmers Who Are Able To Get Along Well With Others.",
                "When This Aspect Of Personality Is Weaker, The Entp May Be Insensitve To Others And Can Even Be Seen As Aloof Or Unkind.",
                "The Introverted Sensing Function Is Centered On Understanding The Past And Often Applying It To Current Experiences And Future Concerns.",
                "This Is Often A Point Of Weakness For Entp Personalities. They Are Often Focused More On Possibilities And May Fail To Consider How Past Precedents May Help Predict Outcomes.",
                "Entps Also Tend To Overlook Many Of The More Mundane Details Of Daily Life, Especially If They Are Deeply Involved In A Project Or Plan."
            ],
            "Strengths": [
                "Innovative",
                "Creative",
                "Great Conversationalist",
                "Enjoys Debating",
                "Values Knowledge"
            ],
            "Weaknesses": [
                "Can Be Argumentative",
                "Dislikes Routines And Schedules",
                "Does Not Like To Be Controlled",
                "Unfocused",
                "Insensitive"
            ],
            "KnownCelbrities": [
                "Thomas Edison, Inventor",
                "John Adams, U.S. President",
                "Walt Disney, Filmmaker",
                "Julia Child, Cook",
                "Alexander The Great, King And Military Leader"
            ],
            "Careers": [
                "Engineer",
                "Lawyer",
                "Scientist",
                "Psychologist",
                "Inventor",
                "Psychiatrist",
                "Journalist"
            ]
        },
        "INFJ": {
            "Type": [
                "Introversion",
                "Intuition",
                "Feeling",
                "Judging"
            ],
            "Name": "Advocate",
            "AltName": "The Advocate",
            "Class": "fas fa-hand-holding-heart",
            "BGColor": "#e57eb1",
            "FTColor": "wheat",
            "Description": "Quiet and mystical, yet very inspiring and tireless idealists.",
            "Dominant": "Introverted Intuition",
            "Auxiliary": "Extraverted Feeling",
            "Tertiary": "Introverted Thinking",
            "Inferior": "Extraverted Sensing",
            "KeyCharacteristics": [
                "With Their Strong Sense Of Intuition And Emotional Understanding, Infjs Can Be Soft-Spoken And Empathetic. This Does Not Mean That They Are Push-Over'S, However. They Have Deeply Held Beliefs And An Ability To Act Decisively In Order To Get What They Want.",
                "While They Are Introverted By Nature, People With This Personality Type Are Able To Form Strong, Meaningful Connections With Other People. They Enjoy Helping Others, But They Also Need Time And Space To Recharge.",
                "While This Personality Type May Be Characterized By Idealism, This Does Not Mean That Infjs See The World Through Rose-Colored Glasses. They Understand The World, Both The Good And The Bad, And Hope To Be Able To Make It Better.",
                "When It Comes To Making Decisions, They Place A Greater Emphasis On Personal Concerns Than Objective Facts When Making Decisions. They Also Like To Exert Control By Planning, Organizing And Making Decisions As Early As Possible.",
                "This Means That They Tend To Be Highly Focused On Their Internal Insights.",
                "Once They Have Formed An Intuition About Something, They Tend To Stick To It Very Tightly, Often To The Point Of Being Single-Minded In Their Focus.",
                "Because Of This, They Are Sometimes Viewed As Being Stubborn And Unyielding.",
                "This Characteristic Of This Type Makes Infjs Highly Aware Of What Other People Are Feeling, But It Means They Are Sometimes Less Aware Of Their Own Emotions.",
                "Infjs Sometimes Struggle To Say No To Other People'S Requests For This Reason. They Are So Attuned To What Other People Are Feeling That They Fear Causing Disappointment Or Hurt Feelings.",
                "Infjs Make Decisions Based On Ideas And Theories That They Form Based On Their Own Insights.",
                "Infjs Rely Primarily On Their Introverted Intuition And Extroverted Feeling When Making Decisions, Particularly When They Are Around Other People. When They Are Alone, However, People With This Personality Type May Rely More On Their Introverted Thinking.",
                "In Stressful Situations, An Infj Might Try To Rely On Emotions When Making Decisions, Especially If It Means Pleasing Other People. Under Less Stressful Conditions, However, An Infj Is More Likely To Rely More On Their Intuition.",
                "While This Is A Less Developed And Largely Unconscious Aspect Of The Infj, It Does Have An Impact On Personality.",
                "This Aspect Of Personality Helps The Infj Pay Attention To The World Around Them And Stay Aware Of Their Surroundings.",
                "Extroverted Sensing Also Helps Infjs Better Live In The Present Moment, Rather Than Simply Worrying About The Future.",
                "This Aspect Of Personality Also Helps Infjs Appreciate Physical Activities Such As Hiking And Dancing."
            ],
            "Strengths": [
                "Sensitive To The Needs Of Others",
                "Reserved",
                "Highly Creative And Artistic",
                "Focused On The Future",
                "Values Close, Deep Relationships",
                "Enjoys Thinking About The Meaning Of Life",
                "Idealistic"
            ],
            "Weaknesses": [
                "Can Be Overly Sensitive",
                "Sometimes Difficult To Get To Know",
                "Can Have Overly High Expectations",
                "Stubborn",
                "Dislikes Confrontation"
            ],
            "KnownCelbrities": [
                "Oprah Winfey, Television Personality",
                "Martin Luther King, Jr., Civil Rights Leader",
                "Atticus Finch, To Kill A Mockingbird",
                "Carl Jung, Psychoanalyst",
                "Taylor Swift, Musician"
            ],
            "Careers": [
                "Artist",
                "Actor",
                "Entrepreneur",
                "Religious Worker",
                "Musician",
                "Librarian",
                "Counselor",
                "Psychologist",
                "Writer",
                "Teacher",
                "Photographer"
            ]
        },
        "INFP": {
            "Type": [
                "Introversion",
                "Intuition",
                "Feeling",
                "Perceiving"
            ],
            "Name": "Mediator",
            "AltName": "The Mediator",
            "Class": "far fa-handshake",
            "BGColor": "#213b60",
            "FTColor": "wheat",
            "Description": "Poetic, kind and altruistic people, always eager to help a good cause.",
            "Dominant": "Introverted Feeling",
            "Auxiliary": "Extraverted Intuition",
            "Tertiary": "Introverted Sensing",
            "Inferior": "Extraverted Thinking",
            "KeyCharacteristics": [
                "Infps Tend To Be Introverted, Quiet, And Reserved. Being In Social Situations Tends To Drain Their Energy And They Prefer Interacting With A Select Group Of Close Friends. While They Like To Be Alone, This Should Not Necessarily Be Confused With Shyness2\\Ufeff . Instead, It Simply Means That Infps Gain Energy From Spending Time Alone. On The Other Hand, They Have To Expend Energy In Social Situations.",
                "Infps Typically Rely On Intuition And Are More Focused On The Big Picture Rather Than The Nitty-Gritty Details. They Can Be Quite Meticulous About Things They Really Care About Or Projects They Are Working On, But Tend To Ignore Mundane Or Boring Details.",
                "Infps Place An Emphasis On Personal Feelings And Their Decisions Are More Influenced By These Concerns Rather Than By Objective Information.",
                "When It Comes To\\U00A0Making Decisions, Infps Like To Keep Their Options Open. They Often Delay Making Important Decisions Just In Case Something About The Situation Changes. When Decisions Are Made, They Are Usually Based On Personal Values Rather Than Logic."
            ],
            "Strengths": [
                "Loyal And Devoted",
                "Sensitive To Feelings",
                "Caring And Interested In Others",
                "Works Well Alone",
                "Values Close Relationships",
                "Good At Seeing The Big Picture"
            ],
            "Weaknesses": [
                "Can Be Overly Idealistic",
                "Tends To Take Everything Personally",
                "Difficult To Get To Know",
                "Sometimes Loses Sight Of The Little Things",
                "Overlooks Details"
            ],
            "KnownCelbrities": [
                "Audrey Hepburn, Actress",
                "Jrr Tolkien, Author",
                "Princess Diana, British Royal",
                "William Shakespeare, Playwright",
                "Fred Rogers, Television Personality"
            ],
            "Careers": [
                "Artist",
                "Counselor",
                "Graphic Designer",
                "Librarian",
                "Psychologist",
                "Physical Therapist",
                "Social Worker",
                "Writer"
            ]
        },
        "ENFJ": {
            "Type": [
                "Extroversion",
                "Intuition",
                "Feeling",
                "Judging"
            ],
            "Name": "Protagonist",
            "AltName": "The Giver",
            "Class": "fas fa-people-arrows",
            "BGColor": "#6f2a4b",
            "FTColor": "wheat",
            "Description": "Charismatic and inspiring leaders, able to mesmerize their listeners.",
            "Dominant": "Extraverted Feeling",
            "Auxiliary": "Introverted Intuition",
            "Tertiary": "Extraverted Sensing",
            "Inferior": "Introverted Thinking",
            "KeyCharacteristics": [
                "Enfjs Are Strong Extraverts; Then Sincerely Enjoy Spending Time With Other People. They Have Great People Skills And Are Often Described As Warm, Affectionate And Supportive. Not Only Are People With This Personality Type Great At Encouraging Other People, They Also Derive Personal Satisfaction From Helping Others.",
                "Enfjs Are Often So Interested In Devoting Their Time To Others That They Can Neglect Their Own Needs. They Also Have A Tendency To Be Too Hard On Themselves, Blaming Themselves For When Things Go Wrong And Not Giving Themselves Enough Credit When Things Go Right. Because Of This, It Is Important That People With This Personality Type Regularly Set Aside Some Time To Attend To Their Own Needs.",
                "They Are Also Good At Bringing Consensus Among Diverse People. For This Reason, They Can Be Outstanding Leaders And Bring An Enthusiasm To A Group That Can Be Motivating And Inspirational.",
                "One Common Myth About Enfjs Is That They Are Always Sociable. While They Love People, They Do Need Time Alone In Order To Assimilate And Organize Their Thoughts."
            ],
            "Strengths": [
                "Outgoing And Warm-Hearted",
                "Empathetic",
                "Wide Social Circle",
                "Encouraging",
                "Organized"
            ],
            "Weaknesses": [
                "Approval-Seeking",
                "Overly Sensitive",
                "Indecisive",
                "Self-Sacrificing"
            ],
            "KnownCelbrities": [
                "Abraham Maslow, Psychologist",
                "Peyton Manning, Football Player",
                "Barack Obama, U.S. President",
                "Bono, Musician",
                "Elizabeth Bennet, Character In Pride And Prejudice"
            ],
            "Careers": [
                "Counselor",
                "Teacher",
                "Psychologist",
                "Social Worker",
                "Human Resources Manager",
                "Sales Representative",
                "Manager"
            ]
        },
        "ENFP": {
            "Type": [
                "Extroversion",
                "Intuition",
                "Feeling",
                "Perceiving"
            ],
            "Name": "Campaigner",
            "AltName": "The Champion",
            "Class": "fas fa-medal",
            "BGColor": "#c90035",
            "FTColor": "wheat",
            "Description": "Enthusiastic, creative and sociable free spirits, who can always find a reason to smile.",
            "Dominant": "Extraverted Intuition",
            "Auxiliary": "Introverted Feeling",
            "Tertiary": "Extraverted Thinking",
            "Inferior": "Introverted Sensing",
            "KeyCharacteristics": [
                "Enfps\\U00A0Have\\U00A0Excellent People Skills. In Addition To Having An Abundance Of Enthusiasm, They Also Genuinely Care About Others. Enfps Are Good At Understanding What Other People Are Feeling. Given Their Zeal, Charisma, And Creativity, They Can Also Make\\U00A0Great Leaders.",
                "People With This Personality Type\\U00A0Strongly Dislike Routine And Prefer To Focus On The Future.2\\Ufeff While They Are Great At Generating New Ideas, They Sometimes Put Off Important Tasks Until The Last Minute. Dreaming Up Ideas But Not Seeing Them Through To Completion Is A Common Problem.",
                "Enfps Can Also Become Easily Distracted, Particularly When They Are Working On Something That Seems Boring Or Uninspiring.",
                "Enfps Are Flexible And Like To Keep Their Options Open. They Can Be Spontaneous And Are Highly Adaptable To Change. They Also Dislike Routine And May Have Problems With Disorganization And Procrastination."
            ],
            "Strengths": [
                "Warm And Enthusiastic",
                "Empathetic And Caring",
                "Strong People Skills",
                "Strong Communication Skills",
                "Fun And Spontaneous",
                "Highly Creative"
            ],
            "Weaknesses": [
                "Needs Approval From Others",
                "Disorganized",
                "Tends To Get Stressed Out Easily",
                "Can Be Overly Emotional",
                "Overthinks",
                "Struggles To Follow Rules"
            ],
            "KnownCelbrities": [
                "Andy Kaufmann, Comedian",
                "Dr. Seuss, Children'S Author",
                "Salvador Dali, Artist",
                "Ellen Degeneres, Comedian And Talk Show Host",
                "Ron Weasley, Harry Potter"
            ],
            "Careers": [
                "Psychologist",
                "Journalist",
                "Actor",
                "Tv Anchor/Reporter",
                "Nutritionist",
                "Nurse",
                "Social Worker",
                "Politician",
                "Counselor"
            ]
        },
        "ISTJ": {
            "Type": [
                "Introversion",
                "Sensing",
                "Thinking",
                "Judging"
            ],
            "Name": "Logistician",
            "AltName": "The Inspector",
            "Class": "far fa-eye",
            "BGColor": "#70c7b8",
            "FTColor": "wheat",
            "Description": "Practical and fact-minded individuals, whose reliability cannot be doubted.",
            "Dominant": "Introverted Sensing",
            "Auxiliary": "Extraverted Thinking",
            "Tertiary": "Introverted Feeling",
            "Inferior": "Extraverted Intuition",
            "KeyCharacteristics": [
                "Istjs Are Planners; They Like To Carefully Plan Things Out Well In Advance. They Enjoy An Orderly Life. They Like Things To Be Well-Organized And Pay A Great Deal Of Attention To Detail. When Things Are In Disarray, People With This Personality Type May Find Themselves Unable To Rest Until They Have Set Everything Straight And The Work Has Been Completed.",
                "Istjs Are Both Responsible And Realistic. They Take A Logical Approach To Achieving Goals And Completing Projects And Are Able To Work At A Steady Pace Toward Accomplishing These Tasks. They Are Able To Ignore Distractions In Order To Focus On The Task At Hand And Are Often Described As Dependable And Trustworthy.",
                "Istjs Also Place A Great Deal Of Emphasis On Traditions And Laws. They Prefer To Follow Rules And Procedures That Have Previously Been Established. In Some Cases, Istjs Can Seem Rigid And Unyielding In Their Desire To Maintain Structure.",
                "Introverted Sensors Are Focused On The Present Moment, Taking In An Abundance Of Information About Their Surroundings.",
                "They Also Have Vivid Memories Of The Past And Rely On The Memories Of These Experiences To Form Expectations For The Future.",
                "Istjs Are Logical And Efficient. They Enjoy Looking For Rational Explanations For Events.",
                "They Prefer To Focus On The Details Rather Than Thinking About Abstract Information.",
                "Being Efficient And Productive Is Important For People With This Personality Type. They Appreciate Knowledge That Has Immediate, Practical Applications.",
                "Istjs Make Decisions Based On Logic And Objective Data Rather Than Personal Feelings.",
                "As They Make Judgments, Istjs Often Make Personal Interpretations Based On Their Internal Set Of Values.",
                "This Is Often Described As An Instinct Or Gut Feeling About A Situation. Istj Might Make A Decision Based On Logic, Only To Have This Feeling Kick In Telling Them To Trust Their Feelings Rather Than Just The Facts.",
                "This Aspect Of Personality Enjoys New Ideas And Experiences.",
                "This Is The Weakest Part Of The Istjs Personality, But Developing This Function Can Sometimes Lead To A More Balanced Personality."
            ],
            "Strengths": [
                "Reliable",
                "Practical",
                "Sensitive",
                "Eye For Detail"
            ],
            "Weaknesses": [
                "Dislikes Abstract Concepts",
                "Avoids Confrontation",
                "Dislikes Change",
                "Neglects Own Needs"
            ],
            "KnownCelbrities": [
                "Mother Teresa, Nun And Humanitarian",
                "Louisa May Alcott, Author",
                "Kristi Yamaguchi, Figure Skater",
                "David Petraeus, U.S. Army General",
                "Dr. John Watson, Sherlock Holmes Series By Arthur Conan Doyle"
            ],
            "Careers": [
                "Social Worker",
                "Counselor",
                "Nurse",
                "Paralegal",
                "Bookkeeper",
                "Child Care Provider",
                "Office Manager",
                "Administrator",
                "Teacher",
                "Banker",
                "Accountant"
            ]
        },
        "ISFJ": {
            "Type": [
                "Introversion",
                "Sensing",
                "Feeling",
                "Judging"
            ],
            "Name": "Defender",
            "AltName": "The Protector",
            "Class": "fas fa-user-shield",
            "BGColor": "#ff5627",
            "FTColor": "wheat",
            "Description": "Very dedicated and warm protectors, always ready to defend their loved ones.",
            "Dominant": "Introverted Sensing",
            "Auxiliary": "Extraverted Feeling",
            "Tertiary": "Introverted Thinking",
            "Inferior": "Extraverted Intuition",
            "KeyCharacteristics": [
                "Isfjs Enjoy Structure And Strive To Maintain This Order In All Areas Of Their Lives. While People With This Personality Type Are Introverted And Tend To Be Quiet, They Are Keen Observers And Are Focused On Other People. Because They Are So Perceptive, Isfjs Are Good At Remembering Details About Other People. Those With This Personality Type Are Particularly Well-Tuned Into The Emotions And Feelings Of Others.",
                "While Isfjs Are Good At Understanding The Emotions, They Often Struggle To Express Their Own Feelings. Rather Than Share Their Feelings, They May Bottle Them Up, Sometimes To The Point That Negative Feelings Toward Other People Can Result. When Dealing With Life Struggles Such As Illness Or The Death Of A Loved One, They May Keep Quiet About What They Are Experiencing In Order To Avoid Burdening Others With Their Troubles.",
                "People With This Personality Prefer Concrete Facts Over Abstract Theories. As A Result, They Tend To Learn Best By Doing. This Also Means That They Usually Value Learning For Its Practical Applications. Isfjs Tend To Become More Interested In New Things When They Can See And Appreciate How It Might Solve A Real-World Problem.",
                "Because Isfjs Tend To Be Protective Of Tradition, There Is A Common Myth That They Are Incapable Of Change. While People With This Personality Type May Not Be Quick To Change, They Are Still Adaptable. They Simply Prefer To Have Time To Think About And Prepare For Big Changes.",
                "This Function Leads The Introverted Sensing Types To Focus On Details And Facts. Isfjs Prefer Concrete Information Rather Than Abstract Theories.",
                "They Are Highly Attuned To The Immediate Environment And Firmly Grounded In Reality.",
                "Because Of This Tendency To Focus On And Protect What Is Familiar, Isfjs Are Often Seen As Highly Traditional.",
                "When Making Decisions, Isfjs Compare Their Vivid Recall Of Past Experiences In Order To Predict The Outcome Of Future Choices And Events.",
                "Isfjs Place A Great Emphasis On Personal Considerations. Extraverted Feelers Are Focused On Developing Social Harmony And Connection. This Is Accomplished Through Behaviors That Are Viewed As Socially Appropriate Or Beneficial, Such As Being Polite, Kind, Considerate, And Helpful.",
                "Isfjs Try To Fill The Wants And Needs Of Other People, Sometimes Even Sacrificing Their Own Desires In Order To Ensure That Other People Are Happy.",
                "Isfjs Are Planners And Tend To Be Very Well-Organized.",
                "This Function Tends To Become Stronger As People Grow Older And Involves Utilizing Logic In Order To Understand How The World Works.",
                "As Isfjs Take In New Information And Experiences, They Look For Connections And Commonalities In Order To Find Patterns.",
                "Rather Than Simply Trying To Understand A Small Part Of Something, They Want To See How Things Fit Together And How It Functions As A Whole.",
                "While Isfjs Tend To Be Focused On The Present And On Concrete Facts, This Largely Unconscious Function Can Help Balance Personality By Helping Focus On Possibilities.",
                "Taking In Facts And Then Explore The What-Ifs Can Lead To New Insights About Problems.",
                "Istjs Are Planners; They Like To Carefully Plan Things Out Well In Advance. They Enjoy An Orderly Life. They Like Things To Be Well-Organized And Pay A Great Deal Of Attention To Detail. When Things Are In Disarray, People With This Personality Type May Find Themselves Unable To Rest Until They Have Set Everything Straight And The Work Has Been Completed.",
                "Istjs Are Both Responsible And Realistic. They Take A Logical Approach To Achieving Goals And Completing Projects And Are Able To Work At A Steady Pace Toward Accomplishing These Tasks. They Are Able To Ignore Distractions In Order To Focus On The Task At Hand And Are Often Described As Dependable And Trustworthy.",
                "Istjs Also Place A Great Deal Of Emphasis On Traditions And Laws. They Prefer To Follow Rules And Procedures That Have Previously Been Established. In Some Cases, Istjs Can Seem Rigid And Unyielding In Their Desire To Maintain Structure.",
                "Introverted Sensors Are Focused On The Present Moment, Taking In An Abundance Of Information About Their Surroundings.",
                "They Also Have Vivid Memories Of The Past And Rely On The Memories Of These Experiences To Form Expectations For The Future.",
                "Istjs Are Logical And Efficient. They Enjoy Looking For Rational Explanations For Events.",
                "They Prefer To Focus On The Details Rather Than Thinking About Abstract Information.",
                "Being Efficient And Productive Is Important For People With This Personality Type. They Appreciate Knowledge That Has Immediate, Practical Applications.",
                "Istjs Make Decisions Based On Logic And Objective Data Rather Than Personal Feelings.",
                "As They Make Judgments, Istjs Often Make Personal Interpretations Based On Their Internal Set Of Values.",
                "This Is Often Describedan Instinct Or Gut Feeling About A Situation. Istj Might Make A Decision Based On Logic, Only To Have This Feeling Kick In Telling Them To Trust Their Feelings Rather Than Just The Facts.",
                "This Aspect Of Personality Enjoys New Ideas And Experiences.",
                "This Is The Weakest Part Of The Istjs Personality, But Developing This Function Can Sometimes Lead To A More Balanced Personality."
            ],
            "Strengths": [
                "Reliable",
                "Practical",
                "Sensitive",
                "Eye For Detail"
            ],
            "Weaknesses": [
                "Dislikes Abstract Concepts",
                "Avoids Confrontation",
                "Dislikes Change",
                "Neglects Own Needs"
            ],
            "KnownCelbrities": [
                "Mother Teresa, Nun And Humanitarian",
                "Louisa May Alcott, Author",
                "Kristi Yamaguchi, Figure Skater",
                "David Petraeus, U.S. Army General",
                "Dr. John Watson, Sherlock Holmes Series By Arthur Conan Doyle"
            ],
            "Careers": [
                "Social Worker",
                "Counselor",
                "Nurse",
                "Paralegal",
                "Bookkeeper",
                "Child Care Provider",
                "Office Manager",
                "Administrator",
                "Teacher",
                "Banker",
                "Accountant"
            ]
        },
        "ESTJ": {
            "Type": [
                "Extroversion",
                "Sensing",
                "Thinking",
                "Judging"
            ],
            "Name": "Executive",
            "AltName": "The Director",
            "Class": "fas fa-user-tie",
            "BGColor": "#f7991c",
            "FTColor": "wheat",
            "Description": "Excellent administrators, unsurpassed at managing things or people.",
            "Dominant": "Extraverted Thinking",
            "Auxiliary": "Introverted Sensing",
            "Tertiary": "Extraverted Intuition",
            "Inferior": "Introverted Feeling",
            "KeyCharacteristics": [
                "Individuals With This Personality Type Tend To Place A High Value On Tradition, Rules, And Security. Maintaining The Status Quo Is Important To Estjs And They Often Become Involved In Civics, Government And Community Organizations.",
                "Because Of Their Orthodox Approach To Life, They Can Sometimes Be Seen As Rigid, Stubborn, And Unyielding. Their Take-Charge Attitude Makes It Easy For Estjs To Assume Leadership Positions.",
                "Their Self-Confidence And Strong Convictions Help Them Excel At Putting Plans Into Action, But They Can At Times Appear Critical And Overly Aggressive, Particular When Other People Fail To Live Up To Their High Standards.",
                "People Often Describe Estjs As Predictable, Stable, Committed, And Practical. They Tend To Be Very Frank And Honest When It Comes To Sharing Their Opinions, Which Can Sometimes Be Seen As Harsh Or Overly Critical.",
                "Estjs Rely On Objective Information And Logic To Make Decisions4\\Ufeff Rather Than Personal Feelings. They Are Skilled At Making Objective, Impersonal Decisions. Rather Than Focusing On Their Own Subjective Feelings When They Are Making Judgments, They Consider Facts And Logic In Order To Make Rational Choices.",
                "People With Estj Personality Types Tend To Be Very Practical. They Enjoy Learning About Things That They Can See An Immediate, Real-World Use For But Tend To Lose Interest In Things That Are Abstract Or Theoretical. Estjs Enjoy Concrete Facts4\\Ufeff As Opposed To Abstract Information.",
                "They Are Good At Making Fast And Decisive Choices, But They May Often Rush To Judgment Before Considering All The Information About A Situation. One The Positive Side, This Trait Makes Them Good Leaders, But It Can Sometimes Lead Them To Being Viewed As Harsh Or Abrasive.",
                "They Are Good At Remembering Things With A Great Deal Of Detail. Their Memories Of Past Events Can Be Quite Vivid And They Often Utilize Their Recollections Of Past Experiences To Make Connections With Present Events.",
                "Because Their Sensing Function Is Focused Inwardly, They Tend To Be Less Concerned With Novelty And More Focused On Familiarity. They Enjoy Having Habits And Routines That They Can Depend Upon. While This Gives Them Stability And Predictability, It Can Also Make Them Stubborn And Unyielding At Times.",
                "This Aspect Of Personality Seeks Out Novel Ideas And Possibilities. It Compels People With This Personality Type To Explore Their Creativity.",
                "As They Process New Ideas And Information, They May Explore The Possible Meanings In Order To Spot New Connections Or Patterns. This Allows Them To Look At Incoming Information And Recognize That There May Be More Than One Interpretation Or Possible Outcome.",
                "When This Function Is Used, It May Lead Estjs To Make Decisions Based More On Feelings Than On Logic. These Are Often Internal Valuations That Lead To Gut Feelings About Some Situations. While This Function Is Not Used As Often, In Some Cases A Person Might Allow Their Subjective Feelings To Override Their Objective Interpretation Of A Situation.",
                "Estjs Tend To Give Much Thought To Their Own Emotions, So This Function Often Operates On A Largely Unconscious Basis."
            ],
            "Strengths": [
                "Practical And Realistic",
                "Dependable",
                "Self-Confident",
                "Hard-Working",
                "Traditional",
                "Strong Leadership Skills"
            ],
            "Weaknesses": [
                "Insensitive",
                "Inflexible",
                "Not Good At Expressing Feelings",
                "Argumentative",
                "Bossy"
            ],
            "KnownCelbrities": [
                "Lyndon B. Johnson, U.S. President",
                "Megyn Kelly, Television Personality",
                "Billy Graham, Evangelist",
                "Alec Baldwin, Actor",
                "Darth Vader, Character From Star Wars"
            ],
            "Careers": [
                "Police Officer",
                "Military",
                "Judge",
                "Teacher",
                "School Administrator",
                "Business Manager",
                "Accountant",
                "Banker"
            ]
        },
        "ESFJ": {
            "Type": [
                "Extroversion",
                "Sensing",
                "Feeling",
                "Judging"
            ],
            "Name": "Consul",
            "AltName": "The Caregiver",
            "Class": "fas fa-hands-helping",
            "BGColor": "#f0574b",
            "FTColor": "wheat",
            "Description": "Extraordinarily caring, social and popular people, always eager to help.",
            "Dominant": "Extraverted Feeling",
            "Auxiliary": "Introverted Sensing",
            "Tertiary": "Extraverted Intuition",
            "Inferior": "Introverted Thinking",
            "KeyCharacteristics": [
                "In Addition To Deriving Pleasure From Helping Others, Esfjs Also \\U200Bhave A Need For Approval. They Expect Their Kind And Giving Ways To Be Noticed And Appreciated By Others. They Are Sensitive To The Needs And Feelings Of Others And Are Good At Responding And Providing The Care That People Need. They Want To Be Liked By Others And Are Easily Hurt By Unkindness Or Indifference.",
                "Esfjs Derive Their Value System From External Sources Including The Community At Large Rather Than From Intrinsic, Ethical, And Moral Guidelines. People With This Personality Type Who Are Raised With High Values And Standards Grow Up To Be Generous Adults. Esfjs Raised In A Less Enriched Environment May Have Skewed Ethics As Adults And Are More Likely To Be Manipulative And Self-Centered.",
                "Esfjs Also Have A Strong Desire To Exert Control Over Their Environment. Organizing, Planning, And Scheduling Help People With This Personality Type Feel In Command Of The World Around Them.",
                "Esfjs Are Naturally Geared Toward Understanding Other People. They Are Careful Observers Of Others And Are Adept At Supporting And Bringing Out The Best In People. Because They Are So Good At Helping Others Feel Good About Themselves, People Feel Drawn To Esfjs.",
                "One Common Myth About Esfjs Is That They Can Sometimes Be Doormat - Allowing Others To Walk Over Them Out Of A Fear Of Disapproval Or Rejection. While They Are People Pleasers, This Does Not Mean That They Are Pushovers.",
                "Esfjs Tend To Make Decisions Based On Personal Feeling, Emotions, And Concern For Others. They Tend To Think More About The Personal Impact Of A Decision Rather Than Considering Objective Criteria.",
                "Esfjs Tend To Judge People And Situations Based Upon Their Gut Feelings.  They Often Make Snap Decisions As A Result And Are Quick To Share Their Feelings And Opinions. This Tendency Can Be Great In Some Ways, As It Allows Them To Make Choices Rather Quickly. On The Negative Side, It Can Sometimes Lead To Overly Harsh Judgments Of Others.",
                "Esfjs Are More Focused On The Present Than On The Future. They Are Interested In Concrete, Immediate Details Rather Than Abstract Or Theoretical Information.",
                "This Cognitive Function Helps Esfjs Make Connections And Find Creative Solutions To Problems.",
                "Esfjs Are Known To Explore The Possibilities When Looking At A Situation. They Can Often Find Patterns That Allow Them To Gain Insights Into People And Experiences.",
                "Esfjs Are Organized And Like To Plan Things Out In Advance. Planning Helps People With This Personality Type Feel More In Control Of The World Around Them.",
                "This Aspect Of Personality Helps The Esfj Analyze Complex Information, But It Is Often A Point Of Weakness, Especially When It Comes To Making Sense Of Abstract Or Theoretical Concepts."
            ],
            "Strengths": [
                "Kind And Loyal",
                "Outgoing",
                "Organized",
                "Practical And Dependable",
                "Enjoys Helping Others"
            ],
            "Weaknesses": [
                "Needy",
                "Approval-Seeking",
                "Sensitive To Criticism"
            ],
            "KnownCelbrities": [
                "Sally Field, Actress",
                "Sam Walton, Wal-Mart Founder",
                "William Mckinley, U.S. President",
                "Barbara Walters, Television Journalist",
                "Joy, Film Character, Inside Out"
            ],
            "Careers": [
                "Childcare",
                "Nursing",
                "Teaching",
                "Social Work",
                "Counseling",
                "Physician",
                "Receptionist",
                "Bookkeeper",
                "Office Manager"
            ]
        },
        "ISTP": {
            "Type": [
                "Introversion",
                "Sensing",
                "Thinking",
                "Perceiving"
            ],
            "Name": "Virtuoso",
            "AltName": "The Crafter",
            "Class": "fas fa-tools",
            "BGColor": "#c2c0b2",
            "FTColor": "darkslategray",
            "Description": "Bold and practical experimenters, masters of all kinds of tools.",
            "Dominant": "Introverted Thinking",
            "Auxiliary": "Extraverted Sensing",
            "Tertiary": "Introverted Intuition",
            "Inferior": "Extraverted Feeling",
            "KeyCharacteristics": [
                "People With An Istp Personality Are Results-Oriented. When There Is A Problem, They Want To Quickly Understand The Underlying Cause And Implement Some Type Of Solution. Istps Are Often Described As Quiet, But With An Easy-Going Attitude Towards Others.",
                "Istps Enjoy New Experiences And May Often Engage In Thrill-Seeking Or Even Risk-Taking Behaviors. They Often Engage In Risky Or Fast-Paced Hobbies Such As Motorcycling, Hang Gliding, Bungee Jumping, Surfing Or Ice Hockey. In Some Cases, They May Seek Out Adventure By Choosing Careers In Areas Such As Racing, Flying, Or Firefighting.",
                "They Prefer To Make Judgments Based Upon Objective Criteria Rather Than Personal Beliefs Or Values.",
                "Istps Are Not Well Attuned To The Emotional States Of Others, And They Can Sometimes Be Seen As A Bit Insensitive. They Also Distance Themselves From Their Own Emotions, Ignoring Their Feelings Until They Become Overwhelming.",
                "One Common Myth About Istps Is That They Are The Stoic, Silent Type. While They Do Tend To Be Reserved, This Does Not Mean That They Do Not Experience Strong Emotions. Instead, They Are Good At Keeping A Cool Head, Maintaining Their Objectivity, And Coping With Crisis.1\\Ufeff",
                "Istps Spend A Great Deal Of Time Thinking And Dealing With Information In Their Own Heads. This Means They Do Not Spend A Great Deal Of Time Expressing Themselves Verbally, So They Are Often Known As Being Quiet.",
                "It May Seem Like The Istps Approach To Decision-Making Is Very Haphazard, Yet Their Actions Are Actually Based Upon Careful Observation And Thought.",
                "They Deal With The World Rationally And Logically, So They Are Often Focused On Things That Seem Practical And Useful.",
                "Because They Are So Logical, Istps Are Good At Looking At Situations In An Objective Way And Avoiding Subjective Or Emotional Factors When Making Decisions. People With This Personality Type Can Be Difficult To Get To Know, Often Because They Are Focused So Much On Action And Results Rather Than On Emotions.1\\Ufeff",
                "Istps Prefer To Focus On The Present And Take On Things One Day At A Time. They Often Avoid Making Long-Term Commitments And Would Rather Focus On The Here And Now Rather Than Think About Future Plans And Possibilities.",
                "Istps Tend To Be Very Logical And Enjoy Learning And Understanding How Things Operate. They Might Take Apart A Mechanical Device Just To See How It Works.",
                "While They Are Good At Understanding Abstract And Theoretical Information, They Are Not Particularly Interested In Such Things Unless They Can See Some Type Of Practical Application.1\\Ufeff",
                "This Function Often Operates Largely Unconsciously In The Istp Personality. While They Are Not Usually Interested In Abstract Ideas, They May Take Such Concepts And Try To Turn Them Into Action Or Practical Solutions.",
                "It Is This Function That Is Behind The Gut Feelings That Istp Sometimes Experience When Making A Decision. By Synthesizing Information Brought In By The Dominant And Auxiliary Functions, This Aspect Of Personality May Be Responsible For Sudden Aha Moments Of Insight.1\\Ufeff",
                "This Aspect Of Personality Tends To Operate In The Background Of The Istp Personality, But It Can Become More Apparent During Times Of Stress.",
                "During Highly Charged Situations, Istps Can Sometimes Lash Out In Sudden Outbursts Of Emotion. They Often Ignore Their Own Feelings Until Things Reach A Boiling Over Point, Which Can Lead To Displaying Emotions In Ways That Can Seem Inappropriate.1\\Ufeff"
            ],
            "Strengths": [
                "Logical",
                "Learns By Experience",
                "Action-Oriented",
                "Realistic And Practical",
                "Enjoys New Things",
                "Self-Confident And Easy-Going"
            ],
            "Weaknesses": [
                "Difficult To Get To Know",
                "Insensitive",
                "Grows Bored Easily",
                "Risk-Taker",
                "Does Not Like Commitment"
            ],
            "KnownCelbrities": [
                "Clint Eastwood, Actor",
                "Zachary Taylor, U.S. President",
                "Alan Shepherd, Astronaut",
                "Amelia Earhart, Aviator",
                "Han Solo, Star Wars Character"
            ],
            "Careers": [
                "Forensic Science",
                "Engineering",
                "Mechanics",
                "Computer Programming",
                "Carpentry",
                "Law Enforcement",
                "Software Engineer",
                "Video Game Designer",
                "Electrician",
                "Scientist",
                "Pilot",
                "Firefighter"
            ]
        },
        "ISFP": {
            "Type": [
                "Introversion",
                "Sensing",
                "Feeling",
                "Perceiving"
            ],
            "Name": "Adventurer",
            "AltName": "The Artist",
            "Class": "fas fa-palette",
            "BGColor": "#581646",
            "FTColor": "wheat",
            "Description": "Flexible and charming artists, always ready to explore and experience something new.",
            "Dominant": "Introverted Feeling",
            "Auxiliary": "Extraverted Sensing",
            "Tertiary": "Introverted Intuition",
            "Inferior": "Extraverted Thinking",
            "KeyCharacteristics": [
                "Isfps Like To Keep Their Options Open, So They Often Delay Making Decisions In Order To See If Things Might Change Or If New Options Come Up.",
                "According To Myers-Briggs, Isfps Are Kind, Friendly, Sensitive And Quiet. Unlike Extroverts Who Gain Energy From Interacting With Other People, Introverts Must Expend Energy Around Others.2\\Ufeff After Spending Time With People, Introverts Often Find That They Need A Period Of Time Alone. Because Of This, They Typically Prefer To Intermingle With A Small Group Of Close Friends And Family Members.",
                "While They Are Quiet And Reserved, They Are Also Known For Being Peaceful, Caring, And Considerate. Isfps Have An Easy-Going Attitude And Tend To Accept Other People As They Are.",
                "Isfps Like To Focus On The Details. They Spend More Time Thinking About The Here And Now Rather Than Worrying About The Future.",
                "Isfps Tend To Be Doers Rather Than Dreamers. They Dislike Abstract Theories Unless They Can See Some Type Of Practical Application For Them And Prefer Learning Situations That Involve Gaining Hands-On Experience.",
                "Isfps Care More About Personal Concerns Rather Than Objective, Logical Information.",
                "People With This Personality Type Deal With Information And Experiences Based Upon How They Feel About Them.",
                "Isfps Have Their Own Value System And Create Spontaneous Judgments Based Upon How Things Fit With Their Own Idea.",
                "People With Isfp Personalities Are Very In Tune With The World Around Them. They Are Very Much Attuned To Sensory Information And Are Keenly Aware When Even Small Changes Take Place In Their Immediate Environment. Because Of This, They Often Place A High Emphasis On Aesthetics And Appreciate The Fine Arts.",
                "They Are Focused On The Present Moment, Taking In New Information And Then Taking Action. They Have A Strong Sense Of Their Immediate Surroundings, Often Noticing Small Details That Others Might Overlook. When Remembering Events From The Past, They Are Able To Recall Strong Visual Imagery And Sights, Smells, And Sounds Can Evoke Powerful Memories Associated With Those Senses.",
                "This Function Tends To Run In The Background, Feeding Off Of The Extraverted Sensing Function.",
                "As Isfps Take In Details About The World, They Often Develop Gut Feelings About Events And Situations. While They Generally Do Not Like Abstract Concepts Or Ideas, This Introverted Intuition Function May Lead Them To Experience Epiphanies About Themselves And Others.",
                "One Weakness That Isfps May Have Is In Organizing, Although They May Use This Function More Prominently In Certain Situations.",
                "This Function Is All About Looking For The Most Efficient Way To Do Something. An Isfp Might Become Focused On Being Very Precise About The Details And Finding The Most Effective Way To Express An Idea.",
                "Isfps Are Friendly And Get Along Well With Other People, But They Typically Need To Get To Know You Well Before They Really Open Up.",
                "You Can Be A Good Friend To An Isfp By Being Supporting An Accepting Of Who They Are.",
                "Isfps Can Be Light-Hearted And Fun, But They Are Also Quite Intense At Times. Recognize That There Will Be Times When Your Friend Wants To Share And Times When He Or She Will Want To Retreat To A More Personal Space.",
                "Isfp Children Tend To Be Perfectionists And Can Be Their Own Harshest Critics.",
                "Because They Place Such High Expectations On Themselves, They Often Underestimate Or Undervalue Their Own Skills And Talents.",
                "If You Are A Parent To Isfp Child, You Can Help Your Child By Encouraging Them To Be Kind To Themselves And Recognize Their Value.",
                "Isfps Are Very Considerate In Relationships, Often To The Point That They Will Continually Defer To Their Partner.",
                "Because They Are Usually Not Good At Expressing Their Own Feelings And Needs, It Is Important That You Make An Effort To Understand Your Partner.",
                "When Making Decisions, Ensure That Your Partner'S Voice Is Heard And His Or Her Feelings Are Given Equal Weight."
            ],
            "Strengths": [
                "Very Aware Of Their Environment",
                "Practical",
                "Enjoys Hands-On Learning",
                "Loyal To Values And Beliefs"
            ],
            "Weaknesses": [
                "Dislikes Abstract, Theoretical Information",
                "Reserved And Quiet",
                "Strong Need For Personal Space",
                "Dislikes Arguments And Conflict"
            ],
            "KnownCelbrities": [
                "Marilyn Monroe, Actress",
                "Auguste Rodin, Sculptor",
                "David Beckham, Soccer Player",
                "Neil Simon, Playwright",
                "Harry Potter, Fictional Character"
            ],
            "Careers": [
                "Artist",
                "Composer Or Musician",
                "Chef",
                "Designer",
                "Forest Ranger",
                "Nurse",
                "Naturalist",
                "Pediatrician",
                "Psychologist",
                "Social Worker",
                "Teacher",
                "Veterinarian"
            ]
        },
        "ESTP": {
            "Type": [
                "Extroversion",
                "Sensing",
                "Thinking",
                "Perceiving"
            ],
            "Name": "Entrepreneur",
            "AltName": "The Persuader",
            "Class": "fas fa-briefcase",
            "BGColor": "#399069",
            "FTColor": "wheat",
            "Description": "Smart, energetic and very perceptive people, who truly enjoy living on the edge.",
            "Dominant": "Extraverted Sensing",
            "Auxiliary": "Introverted Thinking",
            "Tertiary": "Extraverted Feeling",
            "Inferior": "Introverted Intuition",
            "KeyCharacteristics": [
                "When Confronted By Problems, People With This Personality Type Quickly Look At The Facts And Devise An Immediate Solution. They Tend To Improvise Rather Than Spend A Great Deal Of Time Planning.",
                "Estps Don'T Have A Lot Of Use For Abstract Theories Or Concepts. They Are More Practical, Preferring Straightforward Information That They Can Think About Rationally And Act Upon Immediately.",
                "They Are Very Observant, Often Picking Up On Details That Other People Never Notice. Other People Sometimes Describe Them As Fast-Talkers Who Are Highly Persuasive. In Social Settings, They Often Seem Like They Are A Few Steps Ahead Of The Conversation.",
                "Estps Are Not Planners. They React In The Moment And Can Often Be Quite Impulsive Or Even Risk-Taking. This Leap Before They Look Attitude Can Be Problematic At Times And It May Lead Them To Saying Or Doing Things That They Wish They Could Take Back.",
                "One Common Myth About Estps Is That They Are Reckless. In Some Instances, People With This Personality Type Can Veer Into Reckless Behavior. In Most Cases, However, Estps Act Quickly Based On Their Impressions And Logic.",
                "Because They Are So Focused On The Present World, Estps Tend To Be Realists. They Are Interested In The Sights, Sounds, And Experiences That Are Going On Immediately Around Them, And They Have Little Use For Daydreams Or Flights Of Fancy.",
                "As Sensors, People With This Personality Type Want To Touch, Feel, Hear, Taste And See Anything And Everything That Might Possibly Draw Their Interest. When Learning About Something New, It'S Not Just Enough To Read About It In A Textbook Or Listen To A Lecture They Want To Experience It For Themselves.",
                "Estps Also Have Lots Of Energy, So They Can Become Bored In Situations That Are Tedious Or In Learning Situations That Involve A Great Deal Of Theoretical Information. Estps Are The Quintessential Doers They Get Straight To Work And Are Willing To Take Risks In Order To Get The Job Done.",
                "When Making Judgments About The World, Estps Focus Inwardly Where They Process Information In A Logical And Rational Way. Because This Side Of Personality Is Introverted, It Is Something That People May Not Immediately Notice.",
                "This Inner Sense Of Control Gives Estps A Great Deal Of Self-Discipline. They Are Skilled At Working Independently And Can Be Very Goal-Directed When They Want To Achieve An Objective.",
                "They Have Excellent Observational Skills, Noticing Things That Others May Overlook. As They Take In Information, They Then Apply Their Sense Of Logic To Look For Practical And Immediately Applicable Solutions.",
                "This Function Focuses On Creating Social Harmony And Relationships With Others. While Emotions Are Not An Estps Strongest Suit, They Do Have A Great Need For Social Engagement. They Enjoy Being At The Center Of Attention And Are Good At Establishing A Friendly Rapport With Other People.",
                "While They Are Social, Estps Are Sometimes Less Comfortable Sharing Their Opinions And Judgments With Others. Rather Than Rock The Boat, They Are More Focused On Pleasing Others And Maintaining Harmony.\\U00A0They May Overlook Their Own Needs At Times To Ensure That Other People Are Happy.",
                "This Aspect Of Personality Focuses On Looking At Information In Order To See Patterns And Develop A Gut Feeling About Situations.",
                "This Aspect Of Personality Allows Estps To Gain Impressions Of Incoming Data And Develop A Sense Of The Future. They May Look For Connections That Will Allow Them To Gain A Sense Of What To Expect Will Happen Next.",
                "Intuition Is Not An Estps Strong Suit, But They Will Sometimes Develop Strong Gut Reactions To A Situation That May Actually Be Completely Inaccurate. Because Of This, They May Feel That They Do Not Have Good Instincts."
            ],
            "Strengths": [
                "Gregarious, Funny, And Energetic",
                "Influential And Persuasive",
                "Action-Oriented",
                "Adaptable And Resourceful",
                "Observant"
            ],
            "Weaknesses": [
                "Impulsive",
                "Competitive",
                "Dramatic At Times",
                "Easily Bored",
                "Insensitive"
            ],
            "KnownCelbrities": [
                "Donald Trump, Businessman And U.S. President",
                "Madonna, Singer",
                "Ernest Hemingway, Novelist",
                "Thomas Edison, Inventor",
                "Captain James T. Kirk, Fictional Character, Star Trek"
            ],
            "Careers": [
                "Sales Agent",
                "Marketer",
                "Entrepreneur",
                "Police Officers",
                "Detectives",
                "Computer Support Technician",
                "Paramedic"
            ]
        },
        "ESFP": {
            "Type": [
                "Extroversion",
                "Sensing",
                "Feeling",
                "Perceiving"
            ],
            "Name": "Entertainer",
            "AltName": "The Performer",
            "Class": "fas fa-theater-masks",
            "BGColor": "#f27149",
            "FTColor": "wheat",
            "Description": "Spontaneous, energetic and enthusiastic people.  life is never boring around them.",
            "Dominant": "Extraverted Sensing",
            "Auxiliary": "Introverted Feeling",
            "Tertiary": "Extraverted Thinking",
            "Inferior": "Introverted Intuition",
            "KeyCharacteristics": [
                "Esfps Tend To Be Very Practical And Resourceful. They Prefer To Learn Through Hands-On Experience And Tend To Dislike Book Learning And Theoretical Discussions. Because Of This, Students With Esfp Personality Types Sometimes Struggle In Traditional Classroom Settings. However, They Excel In Situations Where They Are Allowed To Interact With Others Or Learn Through Direct Experience.",
                "Esfps Live Very Much In The Here-And-Now And Sometimes Fail To Think About How Current Actions Will Lead To Long-Term Consequences. They Will Often Rush Into A New Situation And Figure Things Out As They Happen. They Also Tend To Dislike Routine, Enjoy New Experiences, And Are Always Looking For A New Adventure.",
                "In Addition To Having A Strong Awareness Of Their Surroundings, They Are Also Very Understanding And Perceptive When It Comes To Other People. They Are Able To Sense What Others Are Feeling And Know How To Respond. People Tend To Find Them Warm, Sympathetic, And Easygoing.",
                "One Common Myth About Esfps Is That They Are Attention-Seekers. While They Are Fun-Loving And Do Not Shun The Spotlight, They Are More Interested In Simply Living In The Present And Doing What Feels Right At That Moment.",
                "Esfps Prefer To Focus On The Here-And-Now Rather Than Thinking About The Distant Future. They Also Prefer Learning About Concrete Facts Rather Than Theoretical Ideas.",
                "Esfps Don\\U2019T Spend A Lot Of Time Planning And Organizing. Instead, They Like To Keep Their Options Open.",
                "When Solving Problems, They Trust Their Instincts And Put Trust In Their Own Abilities To Come Up With A Solution. While They Are Reasonable And Pragmatic, They Dislike Structure, Order, And Planning. Instead, They Act Spontaneously And Do Not Spend A Great Deal Of Time Coming Up With A Plan Or Schedule.",
                "Esfps Place A Greater Emphasis Personal Feelings Rather Than Logic And Facts When Making Decisions.",
                "People With This Personality Type Have An Internal System Of Values On Which They Base Their Decisions. They Are Very Much Aware Of Their Own Emotions And Are Empathetic Towards Others. They Excel At Putting Themselves In Another Person'S Shoes, So To Speak.",
                "This Function Is Focused On Enforcing Order On The Outside World. It Is Centered On Productivity, Logic, And Results.",
                "Because This Tends To Be A Weaker Aspect Of Personality, Esfps May Not Always Feel Secure Sharing Their Judgments, Especially If They Feel It Will Disrupt The Harmony Of The Group.",
                "While This Is The Least Prominent Aspect Of Personality, This Function Can Help The Esfp Spot Patterns And Make Connections In Things They Have Observed.",
                "Esfps Are Usually Not Particularly Adept At Using Logic To Sort Through Abstract Concepts, But This Sense Can Sometimes Lead To Flashes Of Insight And Epiphanies About The Themselves Or The World."
            ],
            "Strengths": [
                "Optimistic And Gregarious",
                "Enjoys People And Socializing",
                "Focused On The Present, Spontaneous",
                "Practical"
            ],
            "Weaknesses": [
                "Dislikes Abstract Theories",
                "Becomes Bored Easily",
                "Does Not Plan Ahead",
                "Impulsive"
            ],
            "KnownCelbrities": [
                "Bill Clinton, U.S. President",
                "Pablo Picasso, Artist",
                "Mark Cuban, Entrepreneur",
                "Will Smith, Actor",
                "Fred And George Weasley, Fictional Characters From Harry Potter"
            ],
            "Careers": [
                "Artist",
                "Actor",
                "Counselor",
                "Social Worker",
                "Athletic Coach",
                "Child Care Provider",
                "Musician",
                "Psychologist",
                "Human Resources Specialist",
                "Fashion Designer"
            ]
        }
    }

    personality_comp = {
        "INFP:INFP": 4,
        "ENFP:INFP": 4,
        "INFJ:INFP": 4,
        "ENFJ:INFP": 5,
        "INFP:INTJ": 4,
        "ENTJ:INFP": 5,
        "INFP:INTP": 4,
        "ENTP:INFP": 4,
        "INFP:ISFP": 1,
        "ESFP:INFP": 1,
        "INFP:ISTP": 1,
        "ESTP:INFP": 1,
        "INFP:ISFJ": 1,
        "ESFJ:INFP": 1,
        "INFP:ISTJ": 1,
        "ESTJ:INFP": 1,
        "ENFP:INFP": 4,
        "ENFP:ENFP": 4,
        "ENFP:INFJ": 5,
        "ENFJ:ENFP": 4,
        "ENFP:INTJ": 5,
        "ENFP:ENTJ": 4,
        "ENFP:INTP": 4,
        "ENFP:ENTP": 4,
        "ENFP:ISFP": 1,
        "ENFP:ESFP": 1,
        "ENFP:ISTP": 1,
        "ENFP:ESTP": 1,
        "ENFP:ISFJ": 1,
        "ENFP:ESFJ": 1,
        "ENFP:ISTJ": 1,
        "ENFP:ESTJ": 1,
        "INFJ:INFP": 4,
        "ENFP:INFJ": 5,
        "INFJ:INFJ": 4,
        "ENFJ:INFJ": 4,
        "INFJ:INTJ": 4,
        "ENTJ:INFJ": 4,
        "INFJ:INTP": 4,
        "ENTP:INFJ": 5,
        "INFJ:ISFP": 1,
        "ESFP:INFJ": 1,
        "INFJ:ISTP": 1,
        "ESTP:INFJ": 1,
        "INFJ:ISFJ": 1,
        "ESFJ:INFJ": 1,
        "INFJ:ISTJ": 1,
        "ESTJ:INFJ": 1,
        "ENFJ:INFP": 5,
        "ENFJ:ENFP": 4,
        "ENFJ:INFJ": 4,
        "ENFJ:ENFJ": 4,
        "ENFJ:INTJ": 4,
        "ENFJ:ENTJ": 4,
        "ENFJ:INTP": 4,
        "ENFJ:ENTP": 4,
        "ENFJ:ISFP": 5,
        "ENFJ:ESFP": 1,
        "ENFJ:ISTP": 1,
        "ENFJ:ESTP": 1,
        "ENFJ:ISFJ": 1,
        "ENFJ:ESFJ": 1,
        "ENFJ:ISTJ": 1,
        "ENFJ:ESTJ": 1,
        "INFP:INTJ": 4,
        "ENFP:INTJ": 5,
        "INFJ:INTJ": 4,
        "ENFJ:INTJ": 4,
        "INTJ:INTJ": 4,
        "ENTJ:INTJ": 4,
        "INTJ:INTP": 4,
        "ENTP:INTJ": 5,
        "INTJ:ISFP": 3,
        "ESFP:INTJ": 3,
        "INTJ:ISTP": 3,
        "ESTP:INTJ": 3,
        "INTJ:ISFJ": 2,
        "ESFJ:INTJ": 2,
        "INTJ:ISTJ": 2,
        "ESTJ:INTJ": 2,
        "ENTJ:INFP": 5,
        "ENFP:ENTJ": 4,
        "ENTJ:INFJ": 4,
        "ENFJ:ENTJ": 4,
        "ENTJ:INTJ": 4,
        "ENTJ:ENTJ": 4,
        "ENTJ:INTP": 5,
        "ENTJ:ENTP": 4,
        "ENTJ:ISFP": 3,
        "ENTJ:ESFP": 3,
        "ENTJ:ISTP": 3,
        "ENTJ:ESTP": 3,
        "ENTJ:ISFJ": 3,
        "ENTJ:ESFJ": 3,
        "ENTJ:ISTJ": 3,
        "ENTJ:ESTJ": 3,
        "INFP:INTP": 4,
        "ENFP:INTP": 4,
        "INFJ:INTP": 4,
        "ENFJ:INTP": 4,
        "INTJ:INTP": 4,
        "ENTJ:INTP": 5,
        "INTP:INTP": 4,
        "ENTP:INTP": 4,
        "INTP:ISFP": 3,
        "ESFP:INTP": 3,
        "INTP:ISTP": 3,
        "ESTP:INTP": 3,
        "INTP:ISFJ": 2,
        "ESFJ:INTP": 2,
        "INTP:ISTJ": 2,
        "ESTJ:INTP": 5,
        "ENTP:INFP": 4,
        "ENFP:ENTP": 4,
        "ENTP:INFJ": 5,
        "ENFJ:ENTP": 4,
        "ENTP:INTJ": 5,
        "ENTJ:ENTP": 4,
        "ENTP:INTP": 4,
        "ENTP:ENTP": 4,
        "ENTP:ISFP": 3,
        "ENTP:ESFP": 3,
        "ENTP:ISTP": 3,
        "ENTP:ESTP": 3,
        "ENTP:ISFJ": 2,
        "ENTP:ESFJ": 2,
        "ENTP:ISTJ": 2,
        "ENTP:ESTJ": 2,
        "INFP:ISFP": 1,
        "ENFP:ISFP": 1,
        "INFJ:ISFP": 1,
        "ENFJ:ISFP": 5,
        "INTJ:ISFP": 3,
        "ENTJ:ISFP": 3,
        "INTP:ISFP": 3,
        "ENTP:ISFP": 3,
        "ISFP:ISFP": 2,
        "ESFP:ISFP": 2,
        "ISFP:ISTP": 2,
        "ESTP:ISFP": 2,
        "ISFJ:ISFP": 3,
        "ESFJ:ISFP": 5,
        "ISFP:ISTJ": 3,
        "ESTJ:ISFP": 5,
        "ESFP:INFP": 1,
        "ENFP:ESFP": 1,
        "ESFP:INFJ": 1,
        "ENFJ:ESFP": 1,
        "ESFP:INTJ": 3,
        "ENTJ:ESFP": 3,
        "ESFP:INTP": 3,
        "ENTP:ESFP": 3,
        "ESFP:ISFP": 2,
        "ESFP:ESFP": 2,
        "ESFP:ISTP": 2,
        "ESFP:ESTP": 2,
        "ESFP:ISFJ": 5,
        "ESFJ:ESFP": 3,
        "ESFP:ISTJ": 5,
        "ESFP:ESTJ": 3,
        "INFP:ISTP": 1,
        "ENFP:ISTP": 1,
        "INFJ:ISTP": 1,
        "ENFJ:ISTP": 1,
        "INTJ:ISTP": 3,
        "ENTJ:ISTP": 3,
        "INTP:ISTP": 3,
        "ENTP:ISTP": 3,
        "ISFP:ISTP": 2,
        "ESFP:ISTP": 2,
        "ISTP:ISTP": 2,
        "ESTP:ISTP": 2,
        "ISFJ:ISTP": 3,
        "ESFJ:ISTP": 5,
        "ISTJ:ISTP": 3,
        "ESTJ:ISTP": 5,
        "ESTP:INFP": 1,
        "ENFP:ESTP": 1,
        "ESTP:INFJ": 1,
        "ENFJ:ESTP": 1,
        "ESTP:INTJ": 3,
        "ENTJ:ESTP": 3,
        "ESTP:INTP": 3,
        "ENTP:ESTP": 3,
        "ESTP:ISFP": 2,
        "ESFP:ESTP": 2,
        "ESTP:ISTP": 2,
        "ESTP:ESTP": 2,
        "ESTP:ISFJ": 5,
        "ESFJ:ESTP": 3,
        "ESTP:ISTJ": 5,
        "ESTJ:ESTP": 3,
        "INFP:ISFJ": 1,
        "ENFP:ISFJ": 1,
        "INFJ:ISFJ": 1,
        "ENFJ:ISFJ": 1,
        "INTJ:ISFJ": 2,
        "ENTJ:ISFJ": 3,
        "INTP:ISFJ": 2,
        "ENTP:ISFJ": 2,
        "ISFJ:ISFP": 3,
        "ESFP:ISFJ": 5,
        "ISFJ:ISTP": 3,
        "ESTP:ISFJ": 5,
        "ISFJ:ISFJ": 4,
        "ESFJ:ISFJ": 4,
        "ISFJ:ISTJ": 4,
        "ESTJ:ISFJ": 4,
        "ESFJ:INFP": 1,
        "ENFP:ESFJ": 1,
        "ESFJ:INFJ": 1,
        "ENFJ:ESFJ": 1,
        "ESFJ:INTJ": 2,
        "ENTJ:ESFJ": 3,
        "ESFJ:INTP": 2,
        "ENTP:ESFJ": 2,
        "ESFJ:ISFP": 5,
        "ESFJ:ESFP": 3,
        "ESFJ:ISTP": 5,
        "ESFJ:ESTP": 3,
        "ESFJ:ISFJ": 4,
        "ESFJ:ESFJ": 4,
        "ESFJ:ISTJ": 4,
        "ESFJ:ESTJ": 4,
        "INFP:ISTJ": 1,
        "ENFP:ISTJ": 1,
        "INFJ:ISTJ": 1,
        "ENFJ:ISTJ": 1,
        "INTJ:ISTJ": 2,
        "ENTJ:ISTJ": 3,
        "INTP:ISTJ": 2,
        "ENTP:ISTJ": 2,
        "ISFP:ISTJ": 3,
        "ESFP:ISTJ": 5,
        "ISTJ:ISTP": 3,
        "ESTP:ISTJ": 5,
        "ISFJ:ISTJ": 4,
        "ESFJ:ISTJ": 4,
        "ISTJ:ISTJ": 4,
        "ESTJ:ISTJ": 4,
        "ESTJ:INFP": 1,
        "ENFP:ESTJ": 1,
        "ESTJ:INFJ": 1,
        "ENFJ:ESTJ": 1,
        "ESTJ:INTJ": 2,
        "ENTJ:ESTJ": 3,
        "ESTJ:INTP": 5,
        "ENTP:ESTJ": 2,
        "ESTJ:ISFP": 5,
        "ESFP:ESTJ": 3,
        "ESTJ:ISTP": 5,
        "ESTJ:ESTP": 3,
        "ESTJ:ISFJ": 4,
        "ESFJ:ESTJ": 4,
        "ESTJ:ISTJ": 4,
        "ESTJ:ESTJ": 4
    }

    idols = [['Abraham Maslow', ' Psychologist'], ['Alan Shepherd', ' Astronaut'], ['Albert Einstein', ' Scientist'],
             ['Alec Baldwin', ' Actor'], ['Alexander The Great', ' King And Military Leader'],
             ['Amelia Earhart', ' Aviator'], ['Andy Kaufmann', ' Comedian'],
             ['Arnold Schwarzenegger', ' Actor & Politician'], ['Atticus Finch', ' To Kill A Mockingbird'],
             ['Audrey Hepburn', ' Actress'], ['Auguste Rodin', ' Sculptor'], ['Barack Obama', ' U.S. President'],
             ['Barbara Walters', ' Television Journalist'], ['Bill Clinton', ' U.S. President'],
             ['Bill Gates', ' Microsoft Founder'], ['Billy Graham', ' Evangelist'], ['Bono', ' Musician'],
             ['C.S. Lewis', ' Author'], ['Captain James T. Kirk', ' Fictional Character', ' Star Trek'],
             ['Carl Jung', ' Psychoanalyst'], ['Carl Sagan', ' Astronomer'], ['Clint Eastwood', ' Actor'],
             ['Darth Vader', ' Character From Star Wars'], ['David Beckham', ' Soccer Player'],
             ['David Petraeus', ' U.S. Army General'], ['Donald Trump', ' Businessman And U.S. President'],
             ['Dr. John Watson', ' Sherlock Holmes Series By Arthur Conan Doyle'], ['Dr. Seuss', " Children's Author"],
             ['Dwight D. Eisenhower', ' U.S. President'], ['Elizabeth Bennet', ' Character In Pride And Prejudice'],
             ['Ellen Degeneres', ' Comedian And Talk Show Host'], ['Ernest Hemingway', ' Novelist'],
             ['Franklin D. Roosevelt', ' U.S. President'],
             ['Fred And George Weasley', ' Fictional Characters From Harry Potter'],
             ['Fred Rogers', ' Television Personality'], ['Gandalf', ' The Lord Of The Rings'],
             ['Han Solo', ' Star Wars Character'], ['Harry Potter', ' Fictional Character'],
             ['John Adams', ' U.S. President'], ['Joy', ' Film Character', ' Inside Out'], ['Jrr Tolkien', ' Author'],
             ['Julia Child', ' Cook'], ['Kristi Yamaguchi', ' Figure Skater'], ['Lance Armstrong', ' Cyclist'],
             ['Lex Luthor', ' Superman Character'], ['Louisa May Alcott', ' Author'],
             ['Lyndon B. Johnson', ' U.S. President'], ['Madonna', ' Singer'], ['Marilyn Monroe', ' Actress'],
             ['Mark Cuban', ' Entrepreneur'], ['Martin Luther King', ' Jr.', ' Civil Rights Leader'],
             ['Megyn Kelly', ' Television Personality'], ['Mother Teresa', ' Nun And Humanitarian'],
             ['Neil Simon', ' Playwright'], ['Oprah Winfey', ' Television Personality'], ['Pablo Picasso', ' Artist'],
             ['Peyton Manning', ' Football Player'], ['Princess Diana', ' British Royal'],
             ['Ron Weasley', ' Harry Potter'], ['Sally Field', ' Actress'], ['Salvador Dali', ' Artist'],
             ['Sam Walton', ' Wal-Mart Founder'], ['Sheldon Cooper', ' The Big Bang Theory'],
             ['Taylor Swift', ' Musician'], ['Thomas Edison', ' Inventor'], ['Thomas Jefferson', ' U.S. President'],
             ['Tiger Woods', ' Golfer'], ['Vince Lombardi', ' Football Coach'], ['Walt Disney', ' Filmmaker'],
             ['Will Smith', ' Actor'], ['William Mckinley', ' U.S. President'], ['William Shakespeare', ' Playwright'],
             ['Zachary Taylor', ' U.S. President']]

    team = {}

    if team_name is None: team_name = f'Team {Faker().word().capitalize()} {Faker().safe_color_name().capitalize()}'
    ratings = []
    for _ in range(num):
        total = 0
        key = Faker().random.randint(0, len(list(job_titles)) - 1)
        job, occupation = list(job_titles.items())[key]
        team_members = []
        team_compatibility = []
        team_combo = []

        for _ in range(team_size):

            if Random().randint(1, 2) == 1:
                gender = 'Male'
            else:
                gender = 'Female'
            if gender == 'Male':
                name = Faker().name_male()
            else:
                name = Faker().name_female()
            personality = get_personality()
            level = Random().randint(1, 4)
            ethnicity = get_ethnicity()

            key = Faker().random.randint(0, len(list(foods.items())) - 1)
            food = list(foods.items())[key]

            member = {
                "id": Faker().uuid4(),
                "name": name,
                "gender": gender,
                "title": occupation.title(),
                "level": level,
                "salary": 0,
                "age": Random().randint(24, 50),
                "skin_tone": ethnicity[0],
                "ethnicity": ethnicity[1],
                "favorite_color": Faker().safe_color_name().capitalize(),
                "favorite_food": food,
                "favorite_person": idols[Random().randint(0, len(idols) - 1)],
                "status": get_status(),
                "personality": personality,
                "happiness": float(),
                "bonuses": {
                    "job_fit": False,
                    "has_friend": False,
                    "young_success": False
                }
            }

            get_job()

            if job in personality_types[personality]['Careers']:
                member['job_fit'] = True
            if level > 2 and member['age'] < 27:
                member['young_success'] = True

            team_members.append(member)

        max_points = 5
        member_max_points = (team_size - 1) * max_points
        for member1 in team_members:
            ctotal = 0
            mem_comp = []
            team_combo.append(member1['personality'])
            for member2 in team_members:
                if member1 == member2: continue
                key = sorted([member1['personality'], member2['personality']])
                key1 = f"{key[0]}:{key[1]}"
                if key1 in personality_comp:
                    h = {key1: personality_comp[key1]}
                    if h not in team_compatibility:
                        team_compatibility.append(h)
                    ctotal += personality_comp[key1]
                    total += personality_comp[key1]
                member1['happiness'] = int('{:,.0f}'.format(((ctotal / member_max_points) * 100)))
                if member1['favorite_color'] == member2['favorite_color']: pass

        team_percentage = (total / (member_max_points * team_size) * 100)
        team_max_points = member_max_points * team_size

        team = {
            "team_name": team_name,
            "team_company": f"{company} {member['jobavatar']['Location']}",
            "team_role": job.title(),
            "team_size": team_size,
            "team_percentage": '{:,.0f}%'.format(team_percentage),
            "team_points": total,
            "team_max_points": team_max_points,
            "team_combos": sorted(team_combo),
            "team_compatibility": team_compatibility,
            "team_members": team_members,
        }

        ratings.append(team['team_percentage'])
        # team_json = json.dumps(team, indent=2, sort_keys=False)
    return json.dumps(team, indent=2)


class Team:
    def __init__(self):
        pass

    # teams = []
    # infjwin = False
    # while infjwin is False:
    #     team_json = create_team()
    #     for x in team_json['team_members']:
    #         if x['personality'] == 'INFJ':
    #             teams.append(team_json)
    #             print(json.dumps(team_json))
    #             infjwin = True

    # f = open(
    #     'C:\\Users\\aries\\source\\repos\\DapperTest\\DapperGenerator\\ClientApp\\src\\components\\sampleteam.json',
    #     "w")
    # f.write(team_json)
    # f.close()
