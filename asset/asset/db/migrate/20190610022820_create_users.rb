class CreateUsers < ActiveRecord::Migration[5.1]
  def change
    create_table :users do |t|
      t.string :title
      t.text :contents
      t.string :image
      t.string :address
      t.float :latitude
      t.float :longitude
      t.timestamps
    end
  end
end
