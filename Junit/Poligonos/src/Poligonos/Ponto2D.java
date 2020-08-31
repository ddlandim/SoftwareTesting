package Poligonos;

public class Ponto2D {
	private double x,y;

	public Ponto2D(){
		x=0;
		y=0; 
	}

	public Ponto2D(double x, double y){
		this.x=x;
		this.y=y; 
	}

	public double getX(){
		return x; 
	}

	public double getY(){
		return y; 
	}

	public void setX(double x){
		this.x=x; 
	}
	
	public void setY(double y) {
		this.y=y;
	}
	
	public static double DistPontos(Ponto2D p1, Ponto2D p2){
		return (Math.sqrt(Math.pow((p2.x-p1.x),2) + Math.pow((p2.y-p1.y), 2)));
	}
}
