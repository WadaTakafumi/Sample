Rails.application.routes.draw do
  devise_for :logs
  resources :users
  get 'hello/index' => 'hello#index'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
