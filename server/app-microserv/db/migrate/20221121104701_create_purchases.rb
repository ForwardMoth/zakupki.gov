class CreatePurchases < ActiveRecord::Migration[7.0]
  def change
    create_table :purchases do |t|
      t.integer :num
      t.date :placement_date
      t.string :name
      t.string :organization

      t.timestamps
    end
  end
end
