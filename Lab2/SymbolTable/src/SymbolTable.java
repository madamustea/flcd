public class SymbolTable {
    public int currentVal;
    public int nrElements;
    public int[] elems;
    public int size;

    public SymbolTable(){
        this.currentVal=0;
        this.nrElements=2;
    }

    public int hash_Function(String key){
        int index=hash(key) % nrElements;
        return  index;
    }

    public void add(String key){
        int val=this.currentVal;
        int index=this.hash_Function(key);
        int curentElem=this.elems[index];
    }

}
