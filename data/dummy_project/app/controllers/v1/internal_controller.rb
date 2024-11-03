class V1::InternalController < ApplicationController
  def control
    controller = ControlRoomService.new().control
  end
end