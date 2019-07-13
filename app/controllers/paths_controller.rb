class PathsController < ApplicationController
  def Map
  

   @p=eval(`python3 getscore.py`)
  


  end

def create
  sql="SHOW columns FROM initial;"
colList=[]
col=ActiveRecord::Base.connection.execute(sql)
		for i in col do
			colList << i[0] ;
		end



@clist=colList[1..7]



sql="select localities FROM initial;"
colList=[]
col=ActiveRecord::Base.connection.execute(sql)
		for i in col do
			colList << i[0] ;
		end

@loc=colList

 end



def insertdata
type = params[:type]
locality = params[:locality]
puts locality
sql="UPDATE initial SET " + type+" = "+ type +" + 1 where localities = "+ locality.to_str + ";"

col=ActiveRecord::Base.connection.execute(sql)
   @p=eval(`python3 ruby_python.py`)

  render json: {}, status: 200

     #    respond_to do |format|
     #    format.html { redirect_to insert_url ,notice: "hello" }
     #  format.json { head :ok }
     #  format.js   { render :layout => false }
    	# end	
end
 
def test

end




end
