int main()
{
   // From here on, access to heaven is denied.
   setuid( 0 );
   system( "/opt/pynternet/pynternet" );

   return 0;
}
