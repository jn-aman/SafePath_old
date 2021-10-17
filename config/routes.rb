Rails.application.routes.draw do
  get 'paths/Map'
root to: "paths#Map" 
  get 'paths/create'
  get 'paths/insertdata'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
