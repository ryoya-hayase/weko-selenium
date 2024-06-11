import sys

import config
from methods_required_during_testing import *
def test_no_1(driver):
    # log in as System Administrator
    A1(driver, config.system_administrator, config.system_administrator_password)

    # Secret URL Download disable
    set_secret_url(driver, False)

    # transition to Mail Templates and scroll down other mail templates
    transition_to_mail_template(driver)
    mail_lists = driver.find_elements(By.XPATH, '//*[@id="sltBoxListEmail"]')
    other_mail_template_list = mail_lists[1].find_elements(By.TAG_NAME, 'li')
    driver.execute_script('document.querySelectorAll(".scrollbar")[0].scrollBy(0, 1000)')

    # create new mail template
    driver.find_element(By.XPATH, '//*[@id="new_term"]').click()

    # input subject and body
    test_subject = 'テストテンプレート'
    subject = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/input')
    subject.send_keys(test_subject)
    test_body = 'テストテンプレート本文'
    body = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div/div[2]/textarea')
    body.send_keys(test_body)

    # save mail template
    driver.find_element(By.XPATH, '//*[@id="save-btn"]').click()
    time.sleep(1)

    # refresh page
    driver.refresh()

    # redefine elements and get template list after save
    mail_lists = driver.find_elements(By.XPATH, '//*[@id="sltBoxListEmail"]')
    other_mail_template_list_after_save = mail_lists[1].find_elements(By.TAG_NAME, 'li')
    save_template_element = other_mail_template_list_after_save[-1].find_element(By.TAG_NAME, 'a')

    # check if the save is successful
    assert len(other_mail_template_list) + 1 == len(other_mail_template_list_after_save)
    assert save_template_element.text.split('|')[1].strip() == test_subject
    save_template_element.click()
    subject = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/input')
    assert subject.get_attribute('value') == test_subject
    body = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div/div[2]/textarea')
    assert body.get_attribute('value') == test_body

    # scroll down other mail templates
    driver.execute_script('document.querySelectorAll(".scrollbar")[0].scrollBy(0, 1000)')
    save_screenshot(driver, sys._getframe().f_code.co_name)

def test_no_2(driver):
    # log in as System Administrator
    A1(driver, config.system_administrator, config.system_administrator_password)

    # Secret URL Download enable
    set_secret_url(driver, True)

    # transition to Mail Templates
    transition_to_mail_template(driver)

    # find Secret URL Download template for test
    mail_lists = driver.find_elements(By.XPATH, '//*[@id="sltBoxListEmail"]')
    secret_url_mail_template_list = mail_lists[0].find_elements(By.TAG_NAME, 'li')
    target = None
    for template in secret_url_mail_template_list:
        if template.text.split('|')[1].strip().startswith('テスト_'):
            target = template
            break
    if target is None:
        raise Exception('Secret URL Download template for test not found')

    # click test template and edit subject and body
    target.click()
    subject = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/input')
    edited_subject = '編集済_' + subject.get_attribute('value')
    subject.clear()
    subject.send_keys(edited_subject)
    body = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div/div[2]/textarea')
    edited_body = '編集後のテンプレート\n' + body.get_attribute('value')
    body.clear()
    body.send_keys(edited_body)

    # save mail template
    driver.find_element(By.XPATH, '//*[@id="save-btn"]').click()
    time.sleep(1)

    # refresh page
    driver.refresh()

    # redefine elements
    mail_lists = driver.find_elements(By.XPATH, '//*[@id="sltBoxListEmail"]')
    secret_url_mail_template_list = mail_lists[0].find_elements(By.TAG_NAME, 'li')
    target = None
    for template in secret_url_mail_template_list:
        if template.text.split('|')[1].strip() == edited_subject:
            target = template
            break
    if target is None:
        raise Exception('Editing Secret URL Download template failed')

    # check if the save is successful
    target.click()
    subject = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/input')
    assert subject.get_attribute('value') == edited_subject
    body = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div/div[2]/textarea')
    assert body.get_attribute('value') == edited_body

    # scroll up window and body
    driver.execute_script('window.scroll(0, 0)')
    driver.execute_script('document.getElementsByTagName("textarea")[0].scroll(0, 0)')
    save_screenshot(driver, sys._getframe().f_code.co_name)

def test_no_3(driver):
    # log in as System Administrator
    A1(driver, config.system_administrator, config.system_administrator_password)

    # Secret URL Download disable
    set_secret_url(driver, False)

    # transition to Mail Templates
    transition_to_mail_template(driver)

    # find Guest User Request template for test
    mail_lists = driver.find_elements(By.XPATH, '//*[@id="sltBoxListEmail"]')
    guest_user_request_mail_template_list = mail_lists[0].find_elements(By.TAG_NAME, 'li')
    target = None
    for template in guest_user_request_mail_template_list:
        if template.text.split('|')[1].strip().startswith('テスト_'):
            target = template
            break
    if target is None:
        raise Exception('Guest User Request template for test not found')

    # click test template and edit subject and body
    target.click()
    subject = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/input')
    edited_subject = '編集済_' + subject.get_attribute('value')
    subject.clear()
    subject.send_keys(edited_subject)
    body = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div/div[2]/textarea')
    edited_body = '編集後のテンプレート\n' + body.get_attribute('value')
    body.clear()
    body.send_keys(edited_body)

    # save mail template
    driver.find_element(By.XPATH, '//*[@id="save-btn"]').click()
    time.sleep(1)

    # refresh page
    driver.refresh()

    # redefine elements
    mail_lists = driver.find_elements(By.XPATH, '//*[@id="sltBoxListEmail"]')
    guest_user_request_mail_template_list = mail_lists[0].find_elements(By.TAG_NAME, 'li')
    target = None
    for template in guest_user_request_mail_template_list:
        if template.text.split('|')[1].strip() == edited_subject:
            target = template
            break
    if target is None:
        raise Exception('Editing Guest User Request template failed')

    # check if the save is successful
    target.click()
    subject = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/input')
    assert subject.get_attribute('value') == edited_subject
    body = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div/div[2]/textarea')
    assert body.get_attribute('value') == edited_body

    # scroll up window and body
    driver.execute_script('window.scroll(0, 0)')
    driver.execute_script('document.getElementsByTagName("textarea")[0].scroll(0, 0)')
    save_screenshot(driver, sys._getframe().f_code.co_name)

def test_no_4(driver):
    # log in as System Administrator
    A1(driver, config.system_administrator, config.system_administrator_password)

    # Secret URL Download disable
    set_secret_url(driver, False)

    # transition to Mail Templates
    transition_to_mail_template(driver)

    # find Other template for test
    mail_lists = driver.find_elements(By.XPATH, '//*[@id="sltBoxListEmail"]')
    other_template_list = mail_lists[1].find_elements(By.TAG_NAME, 'li')
    target = None
    for template in other_template_list:
        if template.text.split('|')[1].strip().startswith('テスト_'):
            target = template
            break
    if target is None:
        raise Exception('Other template for test not found')

    # click test template and edit subject and body
    target.click()
    subject = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/input')
    edited_subject = '編集済_' + subject.get_attribute('value')
    subject.clear()
    subject.send_keys(edited_subject)
    body = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div/div[2]/textarea')
    edited_body = '編集後のテンプレート\n' + body.get_attribute('value')
    body.clear()
    body.send_keys(edited_body)

    # save mail template
    driver.find_element(By.XPATH, '//*[@id="save-btn"]').click()
    time.sleep(1)

    # refresh page
    driver.refresh()

    # redefine elements
    mail_lists = driver.find_elements(By.XPATH, '//*[@id="sltBoxListEmail"]')
    other_template_list = mail_lists[1].find_elements(By.TAG_NAME, 'li')
    target = None
    for template in other_template_list:
        if template.text.split('|')[1].strip() == edited_subject:
            target = template
            break
    if target is None:
        raise Exception('Editing Other template failed')

    # check if the save is successful
    target.click()
    subject = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/input')
    assert subject.get_attribute('value') == edited_subject
    body = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div/div[2]/textarea')
    assert body.get_attribute('value') == edited_body

    # scroll up window and body
    driver.execute_script('document.getElementsByTagName("textarea")[0].scroll(0, 0)')
    save_screenshot(driver, sys._getframe().f_code.co_name)

def test_no_5(driver):
    # log in as Repository Administrator
    A1(driver, config.repository_administrator, config.repository_administrator_password)

    # transition to restricted access
    transition_to_restricted_access(driver)
    term_box_list = driver.find_element(By.XPATH, '//*[@id="sltBoxListEmail"]')
    term_list = term_box_list.find_elements(By.TAG_NAME, 'li')

    # click Add Button
    driver.find_element(By.XPATH, '//*[@id="new_term"]').click()

    # get target elements
    term_title_jp = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div/div[1]/div[1]/input')
    term_content_jp = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div/div[1]/div[2]/textarea')
    term_title_en = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div/div[2]/div[1]/input')
    term_content_en = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div/div[2]/div[2]/textarea')

    # define input values
    input_title_jp = 'テスト利用規約タイトル'
    input_content_jp = 'テスト利用規約'
    input_title_en = config.term_title
    input_content_en = 'Test Terms and Conditions'

    # set input values
    term_title_jp.send_keys(input_title_jp)
    term_content_jp.send_keys(input_content_jp)
    term_title_en.send_keys(input_title_en)
    term_content_en.send_keys(input_content_en)

    # save Terms and Conditions
    driver.find_element(By.XPATH, '//*[@id="save-btn"]').click()
    time.sleep(1)

    # refresh page
    driver.refresh()
    time.sleep(1)

    # redefine elements and get term list after save
    term_box_list = driver.find_element(By.XPATH, '//*[@id="sltBoxListEmail"]')
    term_list_after_save = term_box_list.find_elements(By.TAG_NAME, 'li')
    save_term_element = term_list_after_save[-1].find_elements(By.TAG_NAME, 'a')[0]

    # check if the save is successful
    assert len(term_list) + 1 == len(term_list_after_save)
    assert save_term_element.text == input_title_en
    save_term_element.click()
    term_title_jp = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div/div[1]/div[1]/input')
    term_content_jp = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div/div[1]/div[2]/textarea')
    term_title_en = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div/div[2]/div[1]/input')
    term_content_en = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div/div[2]/div[2]/textarea')
    assert term_title_jp.get_attribute('value') == input_title_jp
    assert term_content_jp.get_attribute('value') == input_content_jp
    assert term_title_en.get_attribute('value') == input_title_en
    assert term_content_en.get_attribute('value') == input_content_en

    driver.execute_script('window.scrollBy(0, 300)')
    save_screenshot(driver, sys._getframe().f_code.co_name)

def test_no_6(driver):
    # log in as Repository Administrator
    A1(driver, config.repository_administrator, config.repository_administrator_password)

    # transition to restricted access
    transition_to_restricted_access(driver)

    # find term what created by test_no_5
    term_box_list = driver.find_element(By.XPATH, '//*[@id="sltBoxListEmail"]')
    term_list = term_box_list.find_elements(By.TAG_NAME, 'li')
    target = None
    for term in term_list:
        term_title_element = term.find_elements(By.TAG_NAME, 'a')[0]
        if term_title_element.text == config.term_title:
            target = term
            break
    if target is None:
        raise Exception('Term what created by test_no_5 not found')

    # click target term
    target.click()

    # get target elements
    term_title_jp = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div/div[1]/div[1]/input')
    term_content_jp = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div/div[1]/div[2]/textarea')
    term_title_en = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div/div[2]/div[1]/input')
    term_content_en = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div/div[2]/div[2]/textarea')

    # define input values
    input_title_jp = '編集済' + term_title_jp.get_attribute('value')
    input_content_jp = '編集後の利用規約\n' + term_content_jp.get_attribute('value')
    input_title_en = config.edited_term_title
    input_content_en = 'Edited Terms and Conditions\n' + term_content_en.get_attribute('value')

    # set input values
    term_title_jp.clear()
    term_title_jp.send_keys(input_title_jp)
    term_content_jp.clear()
    term_content_jp.send_keys(input_content_jp)
    term_title_en.clear()
    term_title_en.send_keys(input_title_en)
    term_content_en.clear()
    term_content_en.send_keys(input_content_en)

    # save Terms and Conditions
    driver.find_element(By.XPATH, '//*[@id="save-btn"]').click()
    time.sleep(1)

    # refresh page
    driver.refresh()
    time.sleep(1)

    # redefine elements
    term_box_list = driver.find_element(By.XPATH, '//*[@id="sltBoxListEmail"]')
    term_list = term_box_list.find_elements(By.TAG_NAME, 'li')
    target = None
    for term in term_list:
        term_title_element = term.find_elements(By.TAG_NAME, 'a')[0]
        if term_title_element.text == input_title_en:
            target = term
            break
    if target is None:
        raise Exception('Editing Terms and Conditions failed')

    # check if the save is successful
    target.click()
    term_title_jp = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div/div[1]/div[1]/input')
    assert term_title_jp.get_attribute('value') == input_title_jp
    term_content_jp = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div/div[1]/div[2]/textarea')
    assert term_content_jp.get_attribute('value') == input_content_jp
    term_title_en = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div/div[2]/div[1]/input')
    assert term_title_en.get_attribute('value') == input_title_en
    term_content_en = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div/div[2]/div[2]/textarea')
    assert term_content_en.get_attribute('value') == input_content_en

    driver.execute_script('window.scrollBy(0, 300)')
    save_screenshot(driver, sys._getframe().f_code.co_name)

def test_no_7(driver):
    # log in as Repository Administrator
    A1(driver, config.repository_administrator, config.repository_administrator_password)

    # transition to restricted access
    transition_to_restricted_access(driver)

    # find term what created by test_no_5 and edited by test_no_6
    term_box_list = driver.find_element(By.XPATH, '//*[@id="sltBoxListEmail"]')
    term_list = term_box_list.find_elements(By.TAG_NAME, 'li')
    target = None
    for term in term_list:
        term_title_element = term.find_elements(By.TAG_NAME, 'a')[0]
        if term_title_element.text == config.edited_term_title:
            target = term
            break
    if target is None:
        raise Exception('Term what created by test_no_5 and edited by test_no_6 not found')

    # delete target term
    target.find_elements(By.TAG_NAME, 'a')[1].click()

    # save Terms and Conditions
    driver.find_element(By.XPATH, '//*[@id="save-btn"]').click()
    time.sleep(1)

    # refresh page
    driver.refresh()
    time.sleep(1)

    # redefine elements and check if the save is successful
    term_box_list = driver.find_element(By.XPATH, '//*[@id="sltBoxListEmail"]')
    term_list_after_delete = term_box_list.find_elements(By.TAG_NAME, 'li')
    assert len(term_list) - 1 == len(term_list_after_delete)
    target = None
    for term in term_list_after_delete:
        term_title_element = term.find_elements(By.TAG_NAME, 'a')[0]
        if term_title_element.text == config.edited_term_title:
            target = term
            break
    assert target is None

    driver.execute_script('window.scrollBy(0, 300)')
    save_screenshot(driver, sys._getframe().f_code.co_name)

def test_no_8(driver):
    # skip this test
    # NII_WEKO3-240
    pass

def test_no_12(driver):
    # log in as Repository Administrator
    A1(driver, config.repository_administrator, config.repository_administrator_password)

    # transition to restricted access
    transition_to_restricted_access(driver)

    # scroll to Usage Report Reminder Email's location
    usage_report_reminder_email = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[8]/div/div/div')
    reminder_location = usage_report_reminder_email.location
    driver.execute_script('window.scrollTo(0, ' + str(reminder_location['y']) + ')')

    # check if Usage Report Reminder Email exists
    tbody = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[8]/div/div/div/div[2]/div[1]/table/tbody')
    trs = tbody.find_elements(By.TAG_NAME, 'tr')
    assert len(trs) > 0

    save_screenshot(driver, sys._getframe().f_code.co_name)

def test_no_13(driver):
    # log in as Repository Administrator
    A1(driver, config.repository_administrator, config.repository_administrator_password)

    # transition to restricted access
    transition_to_restricted_access(driver)

    # scroll to Usage Report Reminder Email's location
    usage_report_reminder_email = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[8]/div/div/div')
    reminder_location = usage_report_reminder_email.location
    driver.execute_script('window.scrollTo(0, ' + str(reminder_location['y']) + ')')

    # get Usage Report Reminder Email's data
    tbody = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[8]/div/div/div/div[2]/div[1]/table/tbody')
    trs = tbody.find_elements(By.TAG_NAME, 'tr')
    if len(trs) == 0:
        raise Exception('Usage Report Reminder Email not found')

    # click check box of first reminder
    reminder_check_box = driver.find_element(
        By.XPATH,
        '//*[@id="root"]/div/div[8]/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/input'
    )
    reminder_check_box.click()

    # click Confirm button
    driver.find_element(By.XPATH, '//*[@id="filter_form_submit"]').click()

    # click Send Mail button
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/button[1]').click()
    # mail sending error

    save_screenshot(driver, sys._getframe().f_code.co_name)

def test_no_14(driver):
    # log in as Community Administrator
    A1(driver, config.community_administrator, config.community_administrator_password)

    # access to admin page
    driver.find_element(By.XPATH, '//*[@id="fixed_header"]/div[2]/div/button').click()
    driver.find_element(By.XPATH, '//*[@id="fixed_header"]/div[2]/div/ul/li[6]').click()
    time.sleep(1)

    # open Setting
    driver.find_element(By.XPATH, '/html/body/div/aside/section/ul/li[7]').click()

    setting_menu = driver.find_element(By.XPATH, '/html/body/div/aside/section/ul/li[7]/ul')
    setting_menu_items = setting_menu.find_elements(By.TAG_NAME, 'li')

    # check to see if Restricted Access and Mail Templates exist
    is_exist_restricted_access = False
    is_exist_mail_templates = False
    for item in setting_menu_items:
        target = item.find_element(By.TAG_NAME, 'a')
        if not is_exist_restricted_access:
            is_exist_restricted_access = target.get_attribute('textContent') == 'Restricted Access'
        if not is_exist_mail_templates:
            is_exist_mail_templates = target.get_attribute('textContent') == 'Mail Templates'
        if is_exist_restricted_access and is_exist_mail_templates:
            break

    # assert not exists Restricted Access and Mail Templates
    assert not is_exist_restricted_access
    assert not is_exist_mail_templates

    save_screenshot(driver, sys._getframe().f_code.co_name)

def test_no_15(driver):
    # log in as Contributor
    A1(driver, config.contributor, config.contributor_password)

    # open menu
    driver.find_element(By.XPATH, '//*[@id="fixed_header"]/div[2]/div/button').click()

    menu = driver.find_element(By.XPATH, '//*[@id="fixed_header"]/div[2]/div/ul')
    menu_items = menu.find_elements(By.TAG_NAME, 'li')

    # check to see if Administration exists
    is_exist_administration = False
    for item in menu_items:
        target = item.find_elements(By.TAG_NAME, 'a')
        if len(target) > 0:
            is_exist_administration = target[0].text == 'Administration'
        if is_exist_administration:
            break

    # assert not exists Administration
    assert not is_exist_administration

    save_screenshot(driver, sys._getframe().f_code.co_name)

def test_no_16(driver):
    # log in as general
    A1(driver, config.general, config.general_password)

    # open menu
    driver.find_element(By.XPATH, '//*[@id="fixed_header"]/div[2]/div/button').click()

    menu = driver.find_element(By.XPATH, '//*[@id="fixed_header"]/div[2]/div/ul')
    menu_items = menu.find_elements(By.TAG_NAME, 'li')

    # check to see if Administration exists
    is_exist_administration = False
    for item in menu_items:
        target = item.find_elements(By.TAG_NAME, 'a')
        if len(target) > 0:
            is_exist_administration = target[0].text == 'Administration'
        if is_exist_administration:
            break

    # assert not exists Administration
    assert not is_exist_administration

    save_screenshot(driver, sys._getframe().f_code.co_name)

def save_screenshot(driver, co_name):
    time.sleep(1)
    driver.save_screenshot(config.base_save_folder + d + "_" + co_name + ".png")