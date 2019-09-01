import java.util.*;
public class amazonsum{
    public static void main(String[] args) {
        long n,m,i;
        Dictionary<Long,Integer> d =new Hashtable<Long,Integer>();
        Scanner sc =new Scanner(System.in);
        n=sc.nextLong();
        m=sc.nextLong();
        i=sc.nextLong();
        long l=i,r=i,sum=1+n;
        m--;
        d.put(i,1);
        System.out.println(sum);
        while(m>0){
            i=sc.nextLong();
            if(d.get(i)!=null){
                System.out.println(sum);
                m--;
                continue;
            }
            else if(i>r){
                sum+=i+r;
                r=i;
            }
            else if(i<l){
                sum+=l+i;
                l=i;
            }
            else if(i>l && i<r){
                sum+=2*i;
            }
            d.put(i,1);
            System.out.println(sum);
            m--;
        }

    }
}