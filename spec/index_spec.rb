require 'selenium-webdriver'
require 'rspec'

describe 'index.html' do
  driver = nil
  before { driver = Selenium::WebDriver.for :chrome }
  after { driver.quit if driver }

  define_method :alert do |msg|
    driver.execute_script "window.alert('#{msg}');"
  end

  define_method :current_height do
    driver.execute_script 'return document.body.scrollTop'   
  end

  it 'should show home' do
    driver.get 'http://localhost:1234'
    expect(driver.title).to eq '@rhysd'
  end

  it 'provides side buttons for scrolling to the corresponding section' do
    driver.get 'http://localhost:1234'
    driver.find_element(:id, 'top-link').click
    sleep 4

    expect(driver.current_url).to eq 'http://localhost:1234/#top'
    height = current_height
    expect(height).to eq 0

    driver.find_element(:id, 'language-link').click
    sleep 4

    expect(driver.current_url).to eq 'http://localhost:1234/#language'
    prev, height = height, current_height
    expect(height).to be > prev

    driver.find_element(:id, 'desktop-app-link').click
    sleep 4

    expect(driver.current_url).to eq 'http://localhost:1234/#desktop-app'
    prev, height = height, current_height
    expect(height).to be > prev

    driver.find_element(:id, 'vim-plugin-link').click
    sleep 4

    expect(driver.current_url).to eq 'http://localhost:1234/#vim-plugin'
    prev, height = height, current_height
    expect(height).to be > prev
  end
end

