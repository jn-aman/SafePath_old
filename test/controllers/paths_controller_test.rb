require 'test_helper'

class PathsControllerTest < ActionDispatch::IntegrationTest
  test "should get Map" do
    get paths_Map_url
    assert_response :success
  end

end
