class PurchasesController < ApplicationController
  before_action :set_purchase, only: %i[ show update destroy ]

  # GET /purchases
  def index
    @purchases = Purchase.all

    render json: @purchases
  end

  # GET /purchases/1
  def show
    render json: @purchase
  end

  # POST /purchases
  def create
    @purchase = Purchase.new(purchase_params)

    if @purchase.save
      render json: @purchase, status: :created, location: @purchase
    else
      render json: @purchase.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /purchases/1
  def update
    if @purchase.update(purchase_params)
      render json: @purchase
    else
      render json: @purchase.errors, status: :unprocessable_entity
    end
  end

  # DELETE /purchases/1
  def destroy
    @purchase.destroy
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_purchase
      @purchase = Purchase.find(params[:id])
    end

    # Only allow a list of trusted parameters through.
    def purchase_params
      params.require(:purchase).permit(:num, :placement_date, :name, :organization)
    end
end
