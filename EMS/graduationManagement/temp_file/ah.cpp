#define m_p make_pair
#define p_b push_back
#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
using namespace std;
#define HASHSIZE 90
struct HashTree{		// structure for hash tree
	int value;
	struct HashTree* child[HASHSIZE];
	int end;
	HashTree(){
		end=0;
		for(int i=0;i<HASHSIZE;i++)
			child[i]=NULL;
	}

};
typedef set<int> ItemSet;		//set of itemsets
typedef set<ItemSet> SuperItemSet;		//set of sets of itemsets
typedef ItemSet::iterator ItemSetIter;	//Itemset iterator
typedef SuperItemSet::iterator SuperItemSetIter;	
vector<int> transactions[20000];	//stores all the transactions 
map< ItemSet,int> support;		//counts the support of  itemsets
map<string,int> ItemToNo;		//Assigns each item to an ID
map<int,string> NoToItem;	   //Converts back each ID to a no.
map<pair<ItemSet,ItemSet>,int> rep;		//checks for duplicate rules 重复规则 
int transactionSize;				//Size of transactions
const double minSup = 0.05;			//Minimum support value
const double minConf = 0.1;			//Minimum confidence value
void readData();		//for reading the data from input file and storing it in a vector of transactions
vector<int> split(string s,char delim);		//for splitting the comma separated itemsets of the transaction
SuperItemSet makeL1();		// for making L1						
SuperItemSet generateCk( const SuperItemSet &L );	//generate itemsets with number of items one more than previous
void createHashTree(struct HashTree **head,const SuperItemSet &res,int k); 	//for creating the hash tree
void subsetHash(SuperItemSet &ret,struct HashTree *head,vector<int> arr,int data[],int start,int end,int index,int k); //for support counting using the generated hash tree
SuperItemSet genSubset( const ItemSet &itemset );	//for generating all the subsets of a set 
void showRule( ofstream &outfile, const SuperItemSet &L);	//for showing all the rules of a particular itemcount
void partition( ofstream &outfile,const ItemSet &itemset,ItemSet &P1,ItemSet &P2,ItemSetIter iter);	