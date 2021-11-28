import configparser

conf = configparser.RawConfigParser()
conf.read(".//Configurations/config.ini")

class readConf:

    @staticmethod
    def get_url():
        url = conf.get('baseData', 'url')
        return url

    @staticmethod
    def get_useremail():
        email = conf.get('baseData', 'useremail')
        return email

    @staticmethod
    def get_userpassword():
        password = conf.get('baseData', 'userpassword')
        return password

    @staticmethod
    def get_home_page_title():
        homePageTitle = conf.get('pageTitle', 'homepage')
        return homePageTitle

    @staticmethod
    def get_women_page_title():
        womenPageTitle = conf.get('pageTitle', 'womenpage')
        return womenPageTitle

    @staticmethod
    def get_checkout_page_title():
        checkoutPageTitle = conf.get('pageTitle', 'checkoutpage')
        return checkoutPageTitle

    @staticmethod
    def get_dresses_page_title():
        dressesPageTitle = conf.get('pageTitle', 'dressespage')
        return dressesPageTitle

    @staticmethod
    def get_tshirts_page_title():
        tshirtsPageTitle = conf.get('pageTitle', 'tshirtspage')
        return tshirtsPageTitle

    @staticmethod
    def get_tops_page_title():
        topsPageTitle = conf.get('pageTitle', 'topspage')
        return topsPageTitle

    @staticmethod
    def get_specials_page_title():
        specialsPageTitle = conf.get('pageTitle', 'specialspage')
        return specialsPageTitle

    @staticmethod
    def get_new_products_page_title():
        newProductsPageTitle = conf.get('pageTitle', 'newproductspage')
        return newProductsPageTitle

    @staticmethod
    def get_address_page_title():
        addressPageTitle = conf.get('pageTitle', 'addresspage')
        return addressPageTitle

    @staticmethod
    def get_contact_us_page_title():
        contactUsPageTitle = conf.get('pageTitle', 'contactuspage')
        return contactUsPageTitle

    @staticmethod
    def get_credit_slip_page_title():
        creditSlipPageTitle = conf.get('pageTitle', 'creditslipspage')
        return creditSlipPageTitle

    @staticmethod
    def get_login_page_title():
        loginPageTitle = conf.get('pageTitle', 'loginpage')
        return loginPageTitle

    @staticmethod
    def get_new_user_registration_page_title():
        newUserRegistrationPageTitle = conf.get('pageTitle', 'newuserregistrationpage')
        return newUserRegistrationPageTitle

    @staticmethod
    def get_order_history_page_title():
        orderHistoryPageTitle = conf.get('pageTitle', 'orderhistory')
        return orderHistoryPageTitle

    @staticmethod
    def get_personal_info_page_title():
        personalInfoPageTitle = conf.get('pageTitle', 'personalinfo')
        return personalInfoPageTitle

    @staticmethod
    def get_wishlist_page_title():
        wishlistPageTitle = conf.get('pageTitle', 'wishlistpage')
        return wishlistPageTitle

    @staticmethod
    def get_my_account_page_title():
        myAccountPageTitle = conf.get('pageTitle', 'myaccountpage')
        return myAccountPageTitle

    @staticmethod
    def get_order_confirmation_page_title():
        orderConfirmationPageTitle = conf.get('pageTitle', 'orederconfirmtionpage')
        return orderConfirmationPageTitle

    @staticmethod
    def get_product1_text():
        fadedTShirtText = conf.get('productDesc', 'fadedTShirt')
        return fadedTShirtText

    @staticmethod
    def get_product2_text():
        blouseText = conf.get('productDesc', 'Blouse')
        return blouseText

    @staticmethod
    def get_product3_text():
        printedDress1Text = conf.get('productDesc', 'printedDress1')
        return printedDress1Text

    @staticmethod
    def get_product4_text():
        printedDress2Text = conf.get('productDesc', 'printedDress2')
        return printedDress2Text

    @staticmethod
    def get_product5_text():
        printedSummerDress1Text = conf.get('productDesc', 'printedSummerDress1')
        return printedSummerDress1Text

    @staticmethod
    def get_product6_text():
        printedSummerDress2Text = conf.get('productDesc', 'printedSummerDress2')
        return printedSummerDress2Text

    @staticmethod
    def get_product7_text():
        printedChiffonDressText = conf.get('productDesc', 'printedChiffonDress')
        return printedChiffonDressText

    @staticmethod
    def get_faded_tshirt_price():
        fadedTshirtPrice = conf.get('productPrice', 'fadedTshirt')
        return fadedTshirtPrice

    @staticmethod
    def get_blouse_price():
        blousePrice = conf.get('productPrice', 'blouse')
        return blousePrice

    @staticmethod
    def get_printed_dress1_price():
        printedDress1Price = conf.get('productPrice', 'printedDress1')
        return printedDress1Price

    @staticmethod
    def get_printed_dress2_price():
        printedDress2Price = conf.get('productPrice', 'printedDress2')
        return printedDress2Price

    @staticmethod
    def get_printed_summer_dress1_price():
        printedSummerDress1Price = conf.get('productPrice', 'printedSummerDress1')
        return printedSummerDress1Price

    @staticmethod
    def get_printed_summer_dress2_price():
        printedSummerDress2Price = conf.get('productPrice', 'printedSummerDress2')
        return printedSummerDress2Price

    @staticmethod
    def get_printed_chiffon_dress_price():
        printedChiffonDressPrice = conf.get('productPrice', 'printedChiffonDress')
        return printedChiffonDressPrice

    @staticmethod
    def get_beige_color():
        beigeColor = conf.get('productColor', 'beige')
        return beigeColor

    @staticmethod
    def get_white_color():
        whiteColor = conf.get('productColor', 'white')
        return whiteColor

    @staticmethod
    def get_black_color():
        blackColor = conf.get('productColor', 'black')
        return blackColor

    @staticmethod
    def get_blue_color():
        blueColor = conf.get('productColor', 'blue')
        return blueColor

    @staticmethod
    def get_yellow_color():
        yellowColor = conf.get('productColor', 'yellow')
        return yellowColor

    @staticmethod
    def get_orange_color():
        orangeColor = conf.get('productColor', 'orange')
        return orangeColor

    @staticmethod
    def get_green_color():
        greenColor = conf.get('productColor', 'green')
        return greenColor

    @staticmethod
    def get_pink_color():
        pinkColor = conf.get('productColor', 'pink')
        return pinkColor

    @staticmethod
    def get_small_size():
        smallSize = conf.get('productSize', 'small')
        return smallSize

    @staticmethod
    def get_medium_size():
        mediumSize = conf.get('productSize', 'medium')
        return mediumSize

    @staticmethod
    def get_large_size():
        largeSize = conf.get('productSize', 'large')
        return largeSize

    @staticmethod
    def get_best_sellers_page_title():
        bestSellersPageTitle = conf.get('pageTitle', 'bestsellerspage')
        return bestSellersPageTitle

    @staticmethod
    def get_search_page_title():
        searchPageTitle = conf.get('pageTitle', 'searchpage')
        return searchPageTitle

    @staticmethod
    def get_product_quanity():
        quantity = conf.get('quantity', 'productQuantity')
        return float(quantity)

    @staticmethod
    def get_product1_identifier():
        product1 = conf.get('sku', 'sku1')
        return product1

    @staticmethod
    def get_product2_identifier():
        product2 = conf.get('sku', 'sku2')
        return product2

    @staticmethod
    def get_product3_identifier():
        product3 = conf.get('sku', 'sku3')
        return product3

    @staticmethod
    def get_product4_identifier():
        product4 = conf.get('sku', 'sku4')
        return product4

    @staticmethod
    def get_product5_identifier():
        product5 = conf.get('sku', 'sku5')
        return product5

    @staticmethod
    def get_product6_identifier():
        product6 = conf.get('sku', 'sku6')
        return product6

    @staticmethod
    def get_product7_identifier():
        product7 = conf.get('sku', 'sku7')
        return product7

    @staticmethod
    def get_new_user_form_title():
        formTitle = conf.get('pageTitle', 'newuserformtitle')
        return formTitle

    @staticmethod
    def get_comparison_page_title():
        comparePageTitle = conf.get('pageTitle', 'comparisonpage')
        return comparePageTitle

    @staticmethod
    def get_address_for_update():
        address = conf.get('delivery', 'address')
        return address

    @staticmethod
    def get_city_for_update():
        city = conf.get('delivery', 'city')
        return city

    @staticmethod
    def get_state_for_update():
        state = conf.get('delivery', 'state')
        return state

    @staticmethod
    def get_zip_for_update():
        zip = conf.get('delivery', 'zip')
        return zip

    @staticmethod
    def get_home_phone_for_update():
        homephone = conf.get('delivery', 'homephone')
        return homephone

    @staticmethod
    def get_mobile_phone_for_update():
        mobilephone = conf.get('delivery', 'mobilephone')
        return mobilephone

    @staticmethod
    def get_addressalias_for_update():
        addressalias = conf.get('delivery', 'addressalias')
        return addressalias

    @staticmethod
    def get_billing_addressalias_for_update():
        billingaddressalias = conf.get('delivery', 'billingaddressalias')
        return billingaddressalias

    @staticmethod
    def get_invalid_email():
        invalidEmail = conf.get('baseData', 'invalidemail')
        return invalidEmail

    @staticmethod
    def get_email_for_password_retrieve_error():
        email = conf.get('baseData', 'emailforpasswordretrieveerror')
        return email

    @staticmethod
    def get_product1_code():
        code = conf.get('code', 'product1')
        return code

    @staticmethod
    def get_product2_code():
        code = conf.get('code', 'product2')
        return code

    @staticmethod
    def get_product3_code():
        code = conf.get('code', 'product3')
        return code

    @staticmethod
    def get_product4_code():
        code = conf.get('code', 'product4')
        return code

    @staticmethod
    def get_product5_code():
        code = conf.get('code', 'product5')
        return code

    @staticmethod
    def get_product6_code():
        code = conf.get('code', 'product6')
        return code

    @staticmethod
    def get_product7_code():
        code = conf.get('code', 'product7')
        return code