class User < ActiveRecord::Base
    
    mount_uploader :image, ImageUploader

    geocoded_by :address
    after_validation :geocode

    # ...
 # 今日投稿された Post を取得
 scope :created_today, -> { where("created_at >= ?", Time.zone.now.beginning_of_day) }
 # または
 # scope :created_today, -> { where(created_at: Time.zone.now.all_day) }

 # 昨日投稿された Post を取得
 scope :created_yesterday, -> { where(created_at: 1.day.ago.all_day) }

 # 3日前に投稿された Post を取得
 scope :created_three_days_ago, -> { where(created_at: 3.days.ago.all_day) }

 # 一週間前に投稿された Post を取得
 scope :created_a_week_ago, -> { where(created_at: 1.week.ago.all_day) }

 # 一ヶ月前に投稿された Post を取得
 scope :created_a_month_ago, -> { where(created_at: 1.month.ago.all_day) }

 # ...
end
