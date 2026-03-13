class Bank 
{
    HashMap<Integer, Long> bank = new HashMap<Integer, Long>();

    public Bank(long[] balance) 
    {
        for(int i = 0; i < balance.length; i++)
        {
            bank.put(i + 1, balance[i]);
        }
    }
    
    public boolean transfer(int account1, int account2, long money) 
    {
        if (!bank.containsKey(account1) || !bank.containsKey(account2)) 
        {
            return false;
        }

        if (bank.get(account1) - money >= 0)
        {
            withdraw(account1, money);
            deposit(account2, money);

            return true;
        }

        return false;
    }
    
    public boolean deposit(int account, long money) 
    {
        if(bank.containsKey(account))
        {
            bank.put(account, bank.get(account) + money);
            return true;
        }
        return false;
    }
    
    public boolean withdraw(int account, long money) 
    {
        if(!bank.containsKey(account))
        {
            return false;
        }
        
        long amount = bank.get(account);
        if (amount - money >= 0)
        {
            bank.put(account, amount - money);
            return true;
        }    
        return false;
    }
}