# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20200523162902) do

  create_table "final", id: false, force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8" do |t|
    t.text   "n",     limit: 65535
    t.bigint "mag"
    t.float  "lati",  limit: 53
    t.float  "longi", limit: 53
  end

  create_table "initial", id: false, force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8" do |t|
    t.text   "localities",               limit: 65535
    t.bigint "assassination"
    t.bigint "theft"
    t.bigint "gang_rape"
    t.bigint "burglary"
    t.bigint "rape"
    t.bigint "assualt_attack"
    t.bigint "harassment"
    t.bigint "crime_total"
    t.float  "area_total",               limit: 53
    t.float  "longitude",                limit: 53
    t.float  "latatitude",               limit: 53
    t.float  "area_per_million_km",      limit: 53
    t.float  "crime_total_divided_area", limit: 53
  end

  create_table "news", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8" do |t|
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

end
