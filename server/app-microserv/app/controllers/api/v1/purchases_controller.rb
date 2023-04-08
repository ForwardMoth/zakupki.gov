class Api::V1::PurchasesController < ApplicationController

    def index
        render json: {"notice_number": "ping", "publication_datetime":"2018-10-10", "name":"name", "fullname":"pong"}, status: 200
    end

    # def get_purchase
    #     @purchase = Purchase.find_by_sql("SELECT notice_number, publication_datetime, name, fullname FROM main_data JOIN customer ON main_data.id = customer.id limit 1;")
    #     render json: @purchase
    # end
end
